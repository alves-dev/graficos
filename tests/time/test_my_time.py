from my_time import DataFrame
import unittest
from constants import DIRECTORY_PLOTAGENS
from datetime import datetime


class TestMyTime(unittest.TestCase):
    df = DataFrame()

    def test_return_name_graphic(self):
        name = self.df.return_name_graphic('test')
        self.assertEqual(name, DIRECTORY_PLOTAGENS + datetime.today().strftime("%Y-%m-%d_%H-%M") + '_' + 'test')
