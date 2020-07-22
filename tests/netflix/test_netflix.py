from netflix import Netflix
from constants import DIRECTORY_PLOTAGENS
from datetime import datetime
import unittest
from graphics.graphic_netflix import GraphicNetflix


class TestNetflix(unittest.TestCase):
    gn = GraphicNetflix(directory='arquivos_testes/NetflixViewingHistory.csv', type_graphic="bars",
                        label_rotation_x='60')
    net = Netflix(graphic_netflix=gn)

    def test_plot(self):
        re = self.net.plot()
        self.assertTrue(re)

    def test_upload_csv(self):
        re = self.net.upload_csv()
        self.assertTrue(re)

    def test_return_name_graphic(self):
        """
        teste da interface_graphic
        :return:
        """
        name = self.gn.return_name_graphic('test')
        self.assertEqual(name, DIRECTORY_PLOTAGENS + datetime.today().strftime("%Y-%m-%d_%H-%M") + '_' + 'test')
