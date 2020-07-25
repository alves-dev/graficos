from typing import Tuple
from constants import DIRECTORY_PLOTAGENS, DIRECTORY_RETORNOS, DIRECTORY_LOGS, DELETE_FILES_DAYS
from os import listdir, remove
from datetime import datetime
import asyncio


class Delete:
    def __init__(self, directory_delete: str):
        self.directory_delete = directory_delete

    async def list_files(self, i) -> Tuple[bool, str]:
        try:
            #directory = listdir('../' + self.directory_delete)
            directory = listdir(self.directory_delete)
            for file in directory:
                print(f'ESSE É {i}')
                print(file)
                if self.verify(file):
                    self.delete(file, self.directory_delete)
                await asyncio.sleep(0.1)

            return True, 'Diretório encontrado'
        except FileNotFoundError as erro:
            return False, f'Diretório não encontrado: {erro}'

    def verify(self, file: str):
        date_str = file.split('_')
        date = datetime.strptime(date_str[0], '%Y-%m-%d').date()
        days = (datetime.now().date() - date).days
        if days > DELETE_FILES_DAYS:
            return True
        return False

    def delete(self, archive: str, directory: str):
        #archive = '../' + directory + archive
        archive = directory + archive
        with open(archive, mode='r') as f:
            remove(archive)

        print(f'DELETADO {archive}')
