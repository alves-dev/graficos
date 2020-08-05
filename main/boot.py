import logging
from datetime import datetime

from utility import Directory


def _config_log(directory):
    name = directory.DIRECTORY_LOGS + datetime.today().strftime("%Y-%m-%d_%H") + '.log'
    logging.basicConfig(filename=name, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S')


class Boot:
    def __init__(self, directory: Directory = Directory()):
        _config_log(directory)
