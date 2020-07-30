import json
from datetime import datetime
import logging


class ReturnJson:
    def __init__(self, directory_returns):
        self.dict_return = {}
        self.DIRECTORY_RETORNOS = directory_returns

    def add_json(self, chave: str, value: object) -> None:
        self.dict_return[chave] = value

    def get_json_dict(self) -> dict:
        return self.dict_return

    def save_json(self) -> bool:
        directory_name = self.DIRECTORY_RETORNOS + datetime.today().strftime("%Y-%m-%d_%H-%M-%S") + '.json'
        with open(directory_name, 'w') as json_file:
            json.dump(self.dict_return, json_file, indent=4, ensure_ascii=False)
            logging.info(f'Arquivo ReturnJson {directory_name} salvo!')
            return True
        return False
