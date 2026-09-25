"""Prueba previa a campo: matriz espuria y señal química genuina."""
import unittest
import csv
import tempfile
from pathlib import Path

import numpy as np

from src.analisis import GRID, evaluate, evaluate_chlorophyll, load_assays, metrics, ridge_predict


def synthetic(real_signal):
    rows = []
    for lake in range(1, 6):
        for point in range(1, 4):
            pigment = 1.5 + lake * 0.8 + point * 0.13
            base = 0.10 + 0.12 * pigment if lake != 5 else 1.2 - 0.12 * pigment
            raw = (0.04 * pigment * np.exp(-((GRID - 665) / 20) ** 2)
                   + 0.015 * pigment * np.exp(-((GRID - 440) / 32) ** 2))
            for level, delta in zip(('0', '2L', '5L', '10L'), (0, 0.1, 0.25, 0.5)):
                colored = np.array([0.4, 0.6, 0.4]) * (base + delta if real_signal else 0.1 * pigment)
                rows.append({'lago_id': f'L{lake:02}', 'muestra_id': f'L{lake:02}-P{point}',
                             'nivel_codigo': level, 'delta_real_mg_l': delta,
                             'referencia_kit_valor': base + delta, 'clorofila_ug_l': 3 * pigment, 'raw': raw.copy(),
                             'colored': colored, 'sensors': np.array([pigment, 12 + lake])})
    return rows


class SyntheticFalsification(unittest.TestCase):
    def test_matrix_correlation_does_not_survive_spike(self):
        rows = synthetic(real_signal=False)
        result = evaluate(rows)
        self.assertAlmostEqual(result['all']['slope_raw'], 0, places=10)
        self.assertAlmostEqual(result['all']['slope_colored'], 0, places=10)
        self.assertIn('sensors_native', result['all'])
        self.assertIn('combined_native', result['all'])
        train = [r for r in rows if r['lago_id'] != 'L05' and r['nivel_codigo'] == '0']
        holdout = [r for r in rows if r['lago_id'] == 'L05' and r['nivel_codigo'] == '0']
        predictions = ridge_predict([r['raw'] for r in train], [r['referencia_kit_valor'] for r in train],
                                    [r['raw'] for r in holdout])
        baseline = np.repeat(np.median([r['referencia_kit_valor'] for r in train]), len(holdout))
        self.assertLess(metrics([r['referencia_kit_valor'] for r in holdout], predictions, baseline)['skill'], 0)

    def test_clorofila_is_positive_control(self):
        rows = [r for r in synthetic(real_signal=False) if r['nivel_codigo'] == '0']
        result = evaluate_chlorophyll(rows)
        self.assertGreater(result['all']['skill'], 0.25)
        self.assertGreaterEqual(sum(v['skill'] > 0 for v in result['by_lake'].values()), 4)

    def test_censored_native_reference_is_not_imputed(self):
        rows = synthetic(real_signal=True)
        for row in rows:
            if row['nivel_codigo'] == '0' and row['muestra_id'].endswith('P1'):
                row['referencia_kit_valor'] = None
        result = evaluate(rows)
        self.assertEqual(result['all']['n_censored'], 5)
        self.assertGreater(result['all']['slope_colored'], 0.8)

    def test_export_pair_subtracts_reagent_blank(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            raw = np.ones(len(GRID)) * 0.1
            blank = np.ones(len(GRID)) * 0.02
            peak = np.exp(-((GRID - 540) / 14) ** 2) * 0.4
            for name, values in [('raw', raw), ('reacted', raw + blank + peak),
                                 ('blank0', np.zeros(len(GRID))), ('blank1', blank)]:
                with (root / f'{name}.csv').open('w', newline='') as handle:
                    writer = csv.writer(handle)
                    writer.writerow(['Pixel', 'Wavelength_nm', 'abs'])
                    writer.writerows((i, wl, value) for i, (wl, value) in enumerate(zip(GRID, values)))
            columns = ['ensayo_id', 'duplicado_tecnico', 'nivel_codigo', 'archivo_espectro_sin',
                       'archivo_espectro_con', 'archivo_blanco_sin', 'archivo_blanco_con',
                       'lambda_kit_nm', 'referencia_kit_valor', 'delta_real_mg_l',
                       'lago_id', 'muestra_id', 'analito', 'kit_sku', 'kit_lote',
                       'especie_reportada', 'referencia_kit_unidad', 'filtrada_045']
            with (root / 'assays.csv').open('w', newline='') as handle:
                writer = csv.DictWriter(handle, fieldnames=columns)
                writer.writeheader()
                writer.writerow({'ensayo_id': 'x', 'duplicado_tecnico': 'NO', 'nivel_codigo': '2L',
                                 'archivo_espectro_sin': 'raw.csv', 'archivo_espectro_con': 'reacted.csv',
                                 'archivo_blanco_sin': 'blank0.csv', 'archivo_blanco_con': 'blank1.csv',
                                 'lambda_kit_nm': 540, 'referencia_kit_valor': 0.2,
                                 'delta_real_mg_l': 0.1, 'lago_id': 'L01', 'muestra_id': 'L01-P1',
                                 'analito': 'nitrito', 'kit_sku': 'synthetic', 'kit_lote': 'lot1',
                                 'especie_reportada': 'NO2-N', 'referencia_kit_unidad': 'mg/L',
                                 'filtrada_045': 'NO'})
            row = load_assays(root / 'assays.csv', root)['nitrito'][0]
            np.testing.assert_allclose(row['raw'], raw)
            np.testing.assert_allclose(row['colored'], peak[[22, 24, 26]])

    def test_reagent_signal_is_recognized_on_unseen_lake(self):
        result = evaluate(synthetic(real_signal=True))
        self.assertAlmostEqual(result['all']['slope_raw'], 0, places=10)
        self.assertGreater(result['all']['colored_all']['skill'], 0.25)
        self.assertGreater(result['all']['slope_colored'], 0.8)
        self.assertLess(result['all']['slope_colored'], 1.2)
        for lake in result['by_lake'].values():
            self.assertGreater(lake['slope_colored'], 0.7)
            self.assertLess(lake['slope_colored'], 1.3)


if __name__ == '__main__':
    unittest.main()
