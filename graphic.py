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
    :return: Uma string com o caminho da imagem gerada
    """

    if type_graphic == 'bars':
        nf.plot_bars(**kwargs)
    elif type_graphic == 'compare':
        nf.plot_compare(**kwargs)
    else:
        print('tipode grafico invalido por isso o compare')
        nf.plot_compare(**kwargs)


    return json


def google():
    pass


netflix(type_graphic='bars', title='netflix', label_rotation_x='55')
