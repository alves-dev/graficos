import unittest
from rules import time_rules


class TestTimeRules(unittest.TestCase):
    csvs = ['arquivos_testes/Historico_tempo_22 - Página1.csv', 'arquivos_testes/Historico_tempo_23 - Página1.csv',
            'arquivos_testes/Historico_tempo_20 - Página1.csv', 'arquivos_testes/Historico_tempo_21 - Página1.csv',
            'arquivos_testes/Historico_tempo_24 - Página1.csv', 'arquivos_testes/Historico_tempo_25 - Página1.csv',
            'arquivos_testes/Historico_tempo_26 - Página1.csv']

    def test_valid_archive_upload(self):
        valid = time_rules.valid_archive_upload(self.csvs)
        valid_false = time_rules.valid_archive_upload('net.doc')
        self.assertTrue(valid and not valid_false, msg='Arquivo não é valido!')
