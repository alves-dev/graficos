import netflix as nf
import json


def netflix(type_graphic: str = 'compare', **kwargs) -> json:
    """
    Define tipo de grafico e parametros

    :param type_graphic: Aceita os valores 'compare' e 'bars'
    :param kwargs:
        :key directory: caminho do csv da netflix
        :key title: titulo do grafico
        :key label_axisx: texto do eixo x
        :key label_axisy: texto do eixo y
        :key label_rotation_x: rotação do texto eixo x, valores {ângulo em graus, 'vertical', 'horizontal'}
        :key box: True ou False para caixa do grafico
        :key type_plot: True ou False para a plotagem no grafico, valido apenas para type_graphic= 'compare'
        :key type_scatter: True ou False para a plotagem no grafico, valido apenas para type_graphic= 'compare'
        :key type_stem: True ou False para a plotagem no grafico, valido apenas para type_graphic= 'compare'
    :return: Uma string com o caminho da imagem gerada
    """
    nf.plot(type_graphic, **kwargs)

    return json


def google():
    pass


netflix(type_plot=True, type_scatter=True)
