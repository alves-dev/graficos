from constants import DIRECTORY_PLOTAGENS
from datetime import datetime


class InterfaceGraphics:
    def __init__(self, type_graphic: str, title: str, label_axisx :str, label_axisy: str, directory):
        self.type_graphic = type_graphic
        self.title = title
        self.label_axisx = label_axisx
        self.label_axisy = label_axisy
        self.directory = directory

    def return_name_graphic(self, name: str) -> str:
        return DIRECTORY_PLOTAGENS + datetime.today().strftime("%Y-%m-%d_%H-%M") + '_' + name
