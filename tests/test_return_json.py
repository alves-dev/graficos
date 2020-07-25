from utility.return_json import ReturnJson
import unittest


class TestReturnJson(unittest.TestCase):
    re = ReturnJson()

    def test_add_json(self):
        self.re.add_json('chave', 'valor')
        self.assertEqual('valor', self.re.get_json_dict()['chave'])

    def test_save_json(self):
        self.re.add_json('chave', 'valor')
        save = self.re.save_json()
        self.assertTrue(save)
