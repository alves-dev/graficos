from typing import Tuple
from utility import Directory
from os import listdir, remove
from datetime import datetime
import asyncio


class Delete:
    def __init__(self, directory: Directory = Directory()):
        self.directory_delete = directory.get_directories()
        self.directory = directory

    async def list_files(self, i) -> Tuple[bool, str]:
        for d in self.directory_delete:
            try:
                directory = listdir(d)
                for file in directory:
                    print(f'ESSE É {i}')
                    print(file)
                    if self.verify(file):
                        self.delete(file, d)
                    await asyncio.sleep(0.1)

            except FileNotFoundError as erro:
                return False, f'Diretório não encontrado: {erro}'
        return True, 'Diretório encontrado'

    def verify(self, file: str):
        date_str = file.split('_')
        date = datetime.strptime(date_str[0], '%Y-%m-%d').date()
        days = (datetime.now().date() - date).days
        if days > self.directory.DELETE_FILES_DAYS:
            return True
        return False

    def delete(self, archive: str, directory: str):
        archive = directory + archive
        with open(archive, mode='r') as f:
            remove(archive)

        print(f'DELETADO {archive}')
