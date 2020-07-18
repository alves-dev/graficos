from netflix import Netflix
from constants import DIRECTORY_PLOTAGENS
from datetime import datetime
import unittest


class TestNetflix(unittest.TestCase):
    net = Netflix()

    def test_plot(self):
        re = self.net.plot(type_graphic="bars")
        self.assertTrue(re)

    def test_upload_csv(self):
        re = self.net.upload_csv()
        self.assertTrue(re)

    def test_return_name_graphic(self):
        name = self.net.return_name_graphic('test')
        self.assertEqual(name, DIRECTORY_PLOTAGENS + datetime.today().strftime("%Y-%m-%d_%H-%M") + '_' + 'test')
