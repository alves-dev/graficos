import os
import sys
sys.path.extend([os.path.dirname(os.path.dirname(os.path.abspath(__file__)))])

from main import Boot
from netflix import Netflix
from my_time import DataFrame
import logging
from utility import Directory
from graphics import GraphicNetflix, GraphicTime
from files import Delete
import asyncio


def netflix(gn: GraphicNetflix) -> dict:
    """
    Define tipo de grafico e parametros

    :return: Uma string com o caminho da imagem gerada
    """

    logging.info('---Iniciado netflix---')
    nf = Netflix(graphic_netflix=gn)
    return_json_dict = nf.plot()
    logging.info('---Finalizado netflix---')

    return return_json_dict


def plot_time(gt: GraphicTime) -> dict:
    """
    Realiza as chamadas dos metodos na ordem...

    :param gt:
    :param directory: Lista dos csv para criar o data frame
        :key index: uma lista de index para serem filtrado = ['04:30:00', ..., '07:30:00']
        :key index_interval: uma lista de dois index para serem filtrado entre eles = ['08:00:00', '17:30:00']
        :key columns: uma lista de datas para serem filtradas = ['10/05/2020',..., '15/05/2020']
        :key columns_days: uma lista de dias da semana para serem filtrado = ['Segunda','terca','']
        :key columns_interval: uma lista contendo datas para serem filtradas entre elas= ['22/12/2019','21/02/2020']
        :key activities: uma lista contendo atividades para serem filtradas = ['Dev', 'Trabalho', 'Descanso', 'TCC']
    :return: ALTERAR O RETORNO PARA UM json
    """

    logging.info('---Iniciado plot_time---')

    df = DataFrame(graphic_time=gt)
    print('data criado')
    #await asyncio.sleep(0.1)
    df.new_data_frame()
    #await asyncio.sleep(0.1)
    df.filters()
    print('filtrado')
    #await asyncio.sleep(0.1)
    df.extract_values()
    print('extraido')
    #await asyncio.sleep(0.1)
    data = df.filter_activities()
    print('activies')
    #await asyncio.sleep(0.1)
    return_json_dict = df.plotar(data=data)

    logging.info('---Finalizado plot_time---')

    return return_json_dict


def main():
    direc = Directory()

    de = Delete(direc)

    '''
    gn = GraphicNetflix(directory='arquivos_testes/NetflixViewingHistory.csv')
    gn2 = GraphicNetflix(directory='arquivos_testes/NetflixViewingHistory.csv', type_graphic='compare')
    netflix(gn=gn)
    netflix(gn=gn2)
    '''

    csvs = ['arquivos_testes/Historico_tempo_2020_48.csv', 'arquivos_testes/Historico_tempo_2020_45.csv',
            'arquivos_testes/Historico_tempo_2020_46.csv', 'arquivos_testes/Historico_tempo_2020_47.csv']

    gt = GraphicTime(directory=csvs, columns_interval=['15/11/2020', '21/11/2020'], type_graphic=['bar_label'],
                     activities=['Trabalho'])
    # activities ['Dev', 'TCC', 'Trabalho', 'Dormir', 'Outros', 'Descanso', 'Faculdade']
    gt2 = GraphicTime(directory=csvs, columns_interval=['22/11/2020', '25/11/2020'],
                      type_graphic=['scatter', 'bar_label'], activities=['Trabalho'],
                      title="Current week's work ")

    #await asyncio.wait([de.list_files(1), plot_time(gt=gt)])

    return_time = plot_time(gt=gt2)
    # print(return_time)


if __name__ == '__main__':
    '''loop = asyncio.get_event_loop()
    loop.run_until_complete(main())'''
    main()
