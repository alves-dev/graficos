from os import path
import os


class Directory:
    def __init__(self, directory_logs='arquivos/logs/', directory_retornos='arquivos/retornos_json/',
                 directory_plotagens='arquivos/plotagens/', delete_files_days=5):
        self.DIRECTORY_LOGS = directory_logs
        self.DIRECTORY_RETORNOS = directory_retornos
        self.DIRECTORY_PLOTAGENS = directory_plotagens
        self.DELETE_FILES_DAYS = delete_files_days
        self.directory_valids = self.verify()

    def get_directories(self):
        return [self.DIRECTORY_LOGS, self.DIRECTORY_PLOTAGENS, self.DIRECTORY_RETORNOS]

    def verify(self) -> bool:
        for d in self.get_directories():
            if not path.exists(d):
                os.mkdir(d)
        return True
