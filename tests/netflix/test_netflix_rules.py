import unittest
from validations import netflix_rules


class TestNetflixRules(unittest.TestCase):

    def test_type_graphic_valid(self):
        valid = netflix_rules.type_graphic_valid('compare')
        self.assertTrue(valid, msg='Não é uma string')

    def test_valid_type_graphic(self):
        valid = netflix_rules.valid_type_graphic('compare')
        valid2 = netflix_rules.valid_type_graphic('bars')
        valid_false = netflix_rules.valid_type_graphic('4')
        self.assertTrue(valid and valid2 and not valid_false, msg='Não é um tipo de grafico valido')

    def test_valid_archive_upload(self):
        valid = netflix_rules.valid_archive_upload('net.csv')
        valid_false = netflix_rules.valid_archive_upload('net.doc')
        self.assertTrue(valid and not valid_false, msg='Arquivo não é valido!')