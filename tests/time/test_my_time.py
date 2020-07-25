from my_time import DataFrame
import unittest
from utils.constants import DIRECTORY_PLOTAGENS
from datetime import datetime
from graphics.graphic_time import GraphicTime


class TestMyTime(unittest.TestCase):
    csvs = ['arquivos_testes/Historico_tempo_22 - Página1.csv', 'arquivos_testes/Historico_tempo_23 - Página1.csv',
            'arquivos_testes/Historico_tempo_20 - Página1.csv', 'arquivos_testes/Historico_tempo_21 - Página1.csv',
            'arquivos_testes/Historico_tempo_24 - Página1.csv', 'arquivos_testes/Historico_tempo_25 - Página1.csv',
            'arquivos_testes/Historico_tempo_26 - Página1.csv']
    gt = GraphicTime(directory=csvs, columns_interval=['10/05/2020', '25/05/2020'], columns_days=['Segunda'],
                     index_interval=['08:00:00', '23:30:00'])
    df = DataFrame(graphic_time=gt)

    def test_return_name_graphic(self):
        name = self.gt.return_name_graphic('test')
        self.assertEqual(name, DIRECTORY_PLOTAGENS + datetime.today().strftime("%Y-%m-%d_%H-%M") + '_' + 'test')
