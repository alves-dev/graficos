from netflix import Netflix
from my_time import DataFrame
import logging
from datetime import datetime
from constants import DIRECTORY_LOGS, DIRECTORY_PLOTAGENS
from graphics import GraphicNetflix, GraphicTime
from files import Delete
import asyncio


def netflix(gn: GraphicNetflix) -> dict:
    """
    Define tipo de grafico e parametros

    :return: Uma string com o caminho da imagem gerada
    """
    config_log()

    logging.info('---Iniciado netflix---')
    nf = Netflix(graphic_netflix=gn)
    return_json_dict = nf.plot()
    logging.info('---Finalizado netflix---')

    return return_json_dict


async def plot_time(gt: GraphicTime) -> dict:
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
    config_log()
    logging.info('---Iniciado plot_time---')

    df = DataFrame(graphic_time=gt)
    print('data criado')
    await asyncio.sleep(0.1)
    df.new_data_frame()
    await asyncio.sleep(0.1)
    df.filters()
    print('filtrado')
    await asyncio.sleep(0.1)
    df.extract_values()
    print('extraido')
    await asyncio.sleep(0.1)
    data = df.filter_activities()
    print('activies')
    await asyncio.sleep(0.1)
    return_json_dict = df.plotar(data=data)

    logging.info('---Finalizado plot_time---')

    return return_json_dict


def config_log():
    logging.basicConfig(filename=DIRECTORY_LOGS + datetime.today().strftime("%Y-%m-%d") + '.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


async def main():

    de = Delete(DIRECTORY_PLOTAGENS)


    gn = GraphicNetflix(directory='arquivos_testes/NetflixViewingHistory.csv')
    netflix(gn=gn)

    csvs = ['arquivos_testes/Historico_tempo_22 - Página1.csv', 'arquivos_testes/Historico_tempo_23 - Página1.csv',
            'arquivos_testes/Historico_tempo_20 - Página1.csv', 'arquivos_testes/Historico_tempo_21 - Página1.csv',
            'arquivos_testes/Historico_tempo_24 - Página1.csv', 'arquivos_testes/Historico_tempo_25 - Página1.csv',
            'arquivos_testes/Historico_tempo_26 - Página1.csv']

    gt = GraphicTime(directory=csvs, columns_interval=['10/05/2020', '25/05/2020'], columns_days=['Segunda'],
                     index_interval=['08:00:00', '23:30:00'], activities=['Dev'])
    # activities ['Dev', 'TCC', 'Trabalho', 'Dormi', 'Outros', 'Descanso', 'Faculdade']
    gt2 = GraphicTime(directory=csvs)
    #return_time = plot_time(gt=gt2)

    await asyncio.wait([de.list_files(1), plot_time(gt=gt2)])
    #print(return_time)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
