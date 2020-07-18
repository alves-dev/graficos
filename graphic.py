from netflix import Netflix
from my_time import DataFrame
import json
import logging
from datetime import datetime
from constants import DIRECTORY_LOGS


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
    config_log()

    logging.info('---Iniciado netflix---')
    nf = Netflix()
    nf.plot(type_graphic, **kwargs)
    logging.info('---Finalizado netflix---')

    return json


def plot_time(directory: list = [], **kwargs) -> dict:
    """
    Realiza as chamadas dos metodos na ordem...

    :param directory: Lista dos csv para criar o data frame
        :key index: uma lista de index para serem filtrado = ['04:30:00', ..., '07:30:00']
        :key index_interval: uma lista de dois index para serem filtrado entre eles = ['08:00:00', '17:30:00']
        :key columns: uma lista de datas para serem filtradas = ['10/05/2020',..., '15/05/2020']
        :key columns_days: uma lista de dias da semana para serem filtrado = ['Segunda','terca','']
        :key columns_interval: uma lista contendo datas para serem filtradas entre elas= ['22/12/2019','21/02/2020']
    :return: ALTERAR O RETORNO PARA UM json
    """
    config_log()
    logging.info('---Iniciado plot_time---')

    df = DataFrame()
    df.new_data_frame(directory=directory)

    df.filters(columns_interval=['10/05/2020', '25/05/2020'], columns_days=['Segunda'],
               index_interval=['08:00:00', '23:30:00'])
    # tm.filters()

    df.extract_values()

    # data = df.filter_activities(['Dev', 'TCC', 'Trabalho', 'Dormi', 'Outros', 'Descanso', 'Faculdade'])
    data = df.filter_activities()

    return_json_dict = df.plotar(data=data, types=['all'])
    logging.info('---Finalizado plot_time---')

    return return_json_dict


def config_log():
    logging.basicConfig(filename=DIRECTORY_LOGS + datetime.today().strftime("%Y-%m-%d") + '.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def main():

    # netflix(type_plot=True, type_scatter=True)
    netflix()

    csvs = ['arquivos_testes/Historico_tempo_22 - Página1.csv', 'arquivos_testes/Historico_tempo_23 - Página1.csv',
            'arquivos_testes/Historico_tempo_20 - Página1.csv', 'arquivos_testes/Historico_tempo_21 - Página1.csv',
            'arquivos_testes/Historico_tempo_24 - Página1.csv', 'arquivos_testes/Historico_tempo_25 - Página1.csv',
            'arquivos_testes/Historico_tempo_26 - Página1.csv']
    return_time = plot_time(directory=csvs)
    # print(return_time)


if __name__ == '__main__':
    main()
