"""Validacion por lago y prueba de adicion patron de MonoSpectro."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

GRID = np.arange(420.0, 781.0, 5.0)
LEVELS = ('0', '2L', '5L', '10L')


def spectrum(path: Path) -> np.ndarray:
    with path.open(newline='', encoding='utf-8-sig') as handle:
        rows = list(csv.DictReader(handle))
    try:
        wl = np.array([float(r['Wavelength_nm']) for r in rows])
        absorbance = np.array([float(r['abs']) for r in rows])
    except (KeyError, ValueError) as exc:
        raise ValueError(f'Espectro invalido: {path}') from exc
    if len(wl) < 2 or not np.isfinite(wl).all() or not np.isfinite(absorbance).all():
        raise ValueError(f'Espectro no finito o incompleto: {path}')
    if not (np.diff(wl) > 0).all() or wl[0] > GRID[0] or wl[-1] < GRID[-1]:
        raise ValueError(f'Eje no creciente o sin cobertura 420-780 nm: {path}')
    return np.interp(GRID, wl, absorbance)


def ridge_predict(x_train, y_train, x_test, alpha=1.0):
    """Escala solo con entrenamiento; la intercepcion queda sin penalizar."""
    x_train = np.asarray(x_train, dtype=float)
    x_test = np.asarray(x_test, dtype=float)
    y_train = np.asarray(y_train, dtype=float)
    if x_train.ndim != 2 or x_test.ndim != 2 or x_train.shape[1] != x_test.shape[1]:
        raise ValueError('Rasgos incompatibles')
    center = x_train.mean(axis=0)
    scale = x_train.std(axis=0)
    scale[scale == 0] = 1
    x = (x_train - center) / scale
    z = (x_test - center) / scale
    target_mean = y_train.mean()
    coefficients = np.linalg.solve(x.T @ x + alpha * np.eye(x.shape[1]), x.T @ (y_train - target_mean))
    return target_mean + z @ coefficients


def metrics(actual, predicted, baseline):
    actual, predicted, baseline = map(lambda a: np.asarray(a, dtype=float), (actual, predicted, baseline))
    mae = float(np.mean(np.abs(actual - predicted)))
    baseline_mae = float(np.mean(np.abs(actual - baseline)))
    ss = float(np.sum((actual - actual.mean()) ** 2))
    return {'n': len(actual), 'mae': mae, 'bias': float(np.mean(predicted - actual)),
            'r2': None if ss == 0 else 1 - float(np.sum((actual - predicted) ** 2)) / ss,
            'skill': None if baseline_mae == 0 else 1 - mae / baseline_mae}


def spike_slope(rows, key):
    """Pendiente forzada a cero de respuesta predicha frente al incremento real."""
    groups = {}
    for row in rows:
        levels = groups.setdefault(row['muestra_id'], {})
        if row['nivel_codigo'] in levels:
            raise ValueError(f"Nivel duplicado: {row['muestra_id']}/{row['nivel_codigo']}")
        levels[row['nivel_codigo']] = row
    numerator = denominator = 0.0
    for sample_id, levels in groups.items():
        if set(levels) != set(LEVELS):
            raise ValueError(f'Serie incompleta: {sample_id}')
        zero = levels['0'][key]
        for level in LEVELS[1:]:
            delta = levels[level]['delta_real_mg_l']
            if delta <= 0:
                raise ValueError(f'Incremento no positivo: {sample_id}/{level}')
            numerator += delta * (levels[level][key] - zero)
            denominator += delta * delta
    return numerator / denominator


def evaluate(rows):
    """Predicciones retenidas por lago; las referencias <L no se imputan."""
    rows = [dict(r) for r in rows]
    lakes = sorted({r['lago_id'] for r in rows})
    if len(lakes) != 5:
        raise ValueError('Se requieren cinco lagos para leave-one-lake-out')
    held = []
    have_sensors = all('sensors' in r for r in rows)
    for lake in lakes:
        train = [r for r in rows if r['lago_id'] != lake]
        test = [r for r in rows if r['lago_id'] == lake]
        native = [r for r in train if r['nivel_codigo'] == '0' and r['referencia_kit_valor'] is not None]
        quantifiable = [r for r in train if r['referencia_kit_valor'] is not None]
        if len(quantifiable) < 2 or not test:
            raise ValueError(f'Pliegue sin referencias cuantificables: {lake}')
        models = [('colored', 'pred_colored', quantifiable)]
        if len(native) >= 2:
            models.append(('raw', 'pred_raw', native))
            if have_sensors:
                models.extend([('sensors', 'pred_sensors', native),
                               ('combined', 'pred_combined', native)])
        for feature, key, subset in models:
            def vector(r):
                return np.r_[r['raw'], r['sensors']] if feature == 'combined' else r[feature]
            predicted = ridge_predict([vector(r) for r in subset],
                                      [r['referencia_kit_valor'] for r in subset],
                                      [vector(r) for r in test])
            for row, value in zip(test, predicted):
                row[key] = float(value)
        raw_baseline = float(np.median([r['referencia_kit_valor'] for r in native])) if native else None
        color_baseline = float(np.median([r['referencia_kit_valor'] for r in quantifiable]))
        for row in test:
            row['base_raw'] = raw_baseline
            row['base_colored'] = color_baseline
        held.extend(test)

    def scored(part, level, prediction, baseline):
        usable = [r for r in part if (level is None or r['nivel_codigo'] == level)
                  and r['referencia_kit_valor'] is not None and prediction in r]
        return (metrics([r['referencia_kit_valor'] for r in usable],
                        [r[prediction] for r in usable], [r[baseline] for r in usable])
                if usable else None)

    def summary(part):
        output = {'n_censored': sum(r['referencia_kit_valor'] is None for r in part),
                  'raw_native': scored(part, '0', 'pred_raw', 'base_raw'),
                  'colored_all': scored(part, None, 'pred_colored', 'base_colored'),
                  'slope_raw': spike_slope(part, 'pred_raw') if all('pred_raw' in r for r in part) else None,
                  'slope_colored': spike_slope(part, 'pred_colored')}
        if have_sensors:
            output['sensors_native'] = scored(part, '0', 'pred_sensors', 'base_raw')
            output['combined_native'] = scored(part, '0', 'pred_combined', 'base_raw')
        return output

    return {'all': summary(held), 'by_lake': {lake: summary([r for r in held if r['lago_id'] == lake]) for lake in lakes}}


def evaluate_chlorophyll(rows):
    rows = list(rows)
    lakes = sorted({r['lago_id'] for r in rows})
    if len(lakes) != 5:
        raise ValueError('Clorofila: se requieren cinco lagos')
    held = []
    for lake in lakes:
        train = [r for r in rows if r['lago_id'] != lake]
        test = [r for r in rows if r['lago_id'] == lake]
        predicted = ridge_predict([r['raw'] for r in train], [r['clorofila_ug_l'] for r in train],
                                  [r['raw'] for r in test])
        baseline = float(np.median([r['clorofila_ug_l'] for r in train]))
        held.extend((lake, r['clorofila_ug_l'], float(p), baseline) for r, p in zip(test, predicted))
    def summarize(part):
        return metrics([r[1] for r in part], [r[2] for r in part], [r[3] for r in part])
    return {'all': summarize(held), 'by_lake': {lake: summarize([r for r in held if r[0] == lake]) for lake in lakes}}


def load_chlorophyll(path: Path, root: Path):
    with path.open(newline='', encoding='utf-8-sig') as handle:
        rows = list(csv.DictReader(handle))
    if any(not r['clorofila_ug_l'] or not r['archivo_espectro_sin'] for r in rows):
        raise ValueError('Clorofila: faltan referencias o espectros')
    return [{'lago_id': r['lago_id'], 'clorofila_ug_l': float(r['clorofila_ug_l']),
             'raw': spectrum(root / r['archivo_espectro_sin'])} for r in rows]


def load_assays(path: Path, root: Path, field_path: Path | None = None):
    sensors = {}
    if field_path:
        with field_path.open(newline='', encoding='utf-8-sig') as handle:
            field_rows = [r for r in csv.DictReader(handle) if r['duplicado_campo'] == 'NO']
        columns = ('temperatura_c', 'conductividad_us_cm', 'ph', 'oxigeno_mg_l', 'turbidez_valor')
        if len({r['turbidez_unidad'] for r in field_rows}) != 1:
            raise ValueError('Unidades de turbidez distintas entre muestras')
        for r in field_rows:
            if any(not r[c] for c in columns):
                raise ValueError(f"Sensores incompletos: {r['muestra_id']}")
            sensors[r['muestra_id']] = np.array([float(r[c]) for c in columns])
    data = {}
    methods = {}
    with path.open(newline='', encoding='utf-8-sig') as handle:
        for row in csv.DictReader(handle):
            if row['duplicado_tecnico'] == 'SI':
                continue  # QC separado; no aumenta n de entrenamiento.
            if row['nivel_codigo'] not in LEVELS:
                raise ValueError(f"Nivel invalido: {row['ensayo_id']}")
            required = ('archivo_espectro_sin', 'archivo_espectro_con', 'lambda_kit_nm',
                        'referencia_kit_valor', 'delta_real_mg_l',
                        'archivo_blanco_sin', 'archivo_blanco_con', 'kit_sku',
                        'kit_lote', 'especie_reportada', 'referencia_kit_unidad', 'filtrada_045')
            if any(not row[k] for k in required):
                raise ValueError(f"Faltan mediciones obligatorias: {row['ensayo_id']}")
            if row['nivel_codigo'] == '0' and float(row['delta_real_mg_l']) != 0:
                raise ValueError(f"Control sin enriquecimiento con delta no nula: {row['ensayo_id']}")
            if row['filtrada_045'] not in ('SI', 'NO'):
                raise ValueError(f"Filtracion invalida: {row['ensayo_id']}")
            method = (row['kit_sku'], row['especie_reportada'], row['referencia_kit_unidad'],
                      float(row['lambda_kit_nm']), row['filtrada_045'])
            old = methods.setdefault(row['analito'], method)
            if old != method:
                raise ValueError(f"Metodo cambia dentro de {row['analito']}")
            raw = spectrum(root / row['archivo_espectro_sin'])
            reacted = spectrum(root / row['archivo_espectro_con'])
            wavelength = float(row['lambda_kit_nm'])
            if not 430 <= wavelength <= 770:
                raise ValueError(f"Longitud de onda fuera de rejilla util: {row['ensayo_id']}")
            blank = spectrum(root / row['archivo_blanco_con']) - spectrum(root / row['archivo_blanco_sin'])
            indices = [int(np.argmin(abs(GRID - (wavelength + offset)))) for offset in (-10, 0, 10)]
            value = row['referencia_kit_valor'].strip()
            reference = None if value in ('<L', '<LOQ') else float(value)
            record = {'lago_id': row['lago_id'], 'muestra_id': row['muestra_id'],
                      'nivel_codigo': row['nivel_codigo'], 'delta_real_mg_l': float(row['delta_real_mg_l']),
                      'referencia_kit_valor': reference,
                      'raw': raw, 'colored': (reacted - raw - blank)[indices]}
            if field_path:
                if row['muestra_id'] not in sensors:
                    raise ValueError(f"Sin sensores: {row['muestra_id']}")
                record['sensors'] = sensors[row['muestra_id']]
            data.setdefault(row['analito'], []).append(record)
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ensayos_csv', type=Path, nargs='?', help='Copia completada de plantillas/ensayos.csv')
    parser.add_argument('--clorofila', type=Path, help='Copia completada de plantillas/clorofila.csv')
    parser.add_argument('--campo', type=Path, help='Copia completada de plantillas/campo.csv, para ablacion de sensores')
    parser.add_argument('--root', type=Path, default=Path.cwd(), help='Raiz para rutas de espectros')
    parser.add_argument('--salida', type=Path, default=Path('resultados/validacion.json'))
    args = parser.parse_args()
    if not args.ensayos_csv and not args.clorofila:
        parser.error('Indica ensayos_csv, --clorofila, o ambos')
    result = {}
    if args.clorofila:
        result['clorofila_a'] = evaluate_chlorophyll(load_chlorophyll(args.clorofila, args.root))
    if args.ensayos_csv:
        result.update({analyte: evaluate(rows) for analyte, rows in load_assays(args.ensayos_csv, args.root, args.campo).items()})
    args.salida.parent.mkdir(parents=True, exist_ok=True)
    args.salida.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(args.salida)


if __name__ == '__main__':
    main()
