import netflix as nf
import my_time as tm
import json
import logging
from datetime import datetime


def netflix(type_graphic: str = 'compare', **kwargs) -> json:
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
    :return: Uma string com o caminho da imagem gerada
    """
    nf.plot(type_graphic, **kwargs)

    return json


def time(directory: list = [], **kwargs) -> json:
    """

    :param directory: Lista dos csv para criar o data frame
    :param
        :key days: uma lista de dias da semana para serem filtrado = ['Segunda','terca','']
        :key dates: uma lista contendo datas para serem filtradas = ['22/12/2019','21/02/2020']
    :return:
    """
    tm.new_data_frame(directory=directory, **kwargs)
    tm.plotar()


def main():
    logging.basicConfig(filename='logs/'+datetime.today().strftime("%Y-%m-%d") + '.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S')

    logging.info('---Iniciado---')
    # netflix(type_plot=True, type_scatter=True)
    csvs = ['Historico_tempo_22 - Página1.csv', 'Historico_tempo_23 - Página1.csv', 'Historico_tempo_20 - Página1.csv']
    time(directory=csvs)
    # netflix()
    logging.info('---Finalizado---')


if __name__ == '__main__':
    main()
