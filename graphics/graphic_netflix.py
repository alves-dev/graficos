from graphics.interface_graphic import InterfaceGraphics
from datetime import datetime
from utility import Directory


class GraphicNetflix(InterfaceGraphics):
    """
        Define tipo de grafico e parametros

    :param type_graphic: Aceita os valores 'compare' e 'bars'
    :param
        :key directory: caminho do csv da netflix
        :key title: titulo do grafico
        :key label_axisx: texto do eixo x
        :key label_axisy: texto do eixo y
        :key label_rotation_x: rotação do texto eixo x, valores {ângulo em graus, 'vertical', 'horizontal'}
        :key box: True ou False para caixa do grafico
        :key type_plot: True ou False para a plotagem no grafico, valido apenas para type_graphic= 'compare'
        :key type_scatter: True ou False para a plotagem no grafico, valido apenas para type_graphic= 'compare'
        :key type_stem: True ou False para a plotagem no grafico, valido apenas para type_graphic= 'compare'
    """

    def __init__(self, directory, type_graphic: str = 'compare', title: str = 'Quantidade de titulos Netflix',
                 label_axisx: str = 'mês/ano', label_axisy: str = 'Quantidade de Titulos',
                 label_rotation_x='horizontal', box: bool = True, type_plot: bool = True, type_scatter: bool = True,
                 type_stem: bool = False, directory_save: Directory = Directory()):
        InterfaceGraphics.__init__(self, type_graphic, title, label_axisx, label_axisy, directory)
        self.label_rotation_x = label_rotation_x
        self.box = box
        self.type_plot = type_plot
        self.type_scatter = type_scatter
        self.type_stem = type_stem
        self.directory_save = directory_save

    def return_name_graphic(self, name: str) -> str:
        return self.directory_save.DIRECTORY_PLOTAGENS + datetime.today().strftime("%Y-%m-%d_%H-%M") + '_' + name
