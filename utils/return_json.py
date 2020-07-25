import json
from datetime import datetime
from utils.constants import DIRECTORY_RETORNOS
import logging


class ReturnJson:
    def __init__(self):
        self.dict_return = {}

    def add_json(self, chave: str, value: object) -> None:
        self.dict_return[chave] = value

    def get_json_dict(self) -> dict:
        return self.dict_return

    def save_json(self) -> bool:
        directory_name = DIRECTORY_RETORNOS + datetime.today().strftime("%Y-%m-%d_%H-%M-%S") + '.json'
        with open(directory_name, 'w') as json_file:
            json.dump(self.dict_return, json_file, indent=4, ensure_ascii=False)
            logging.info(f'Arquivo ReturnJson {directory_name} salvo!')
            return True
        return False
