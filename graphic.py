import netflix as nf
import my_time as tm
import json
import logging
from datetime import datetime
from constants import DIRECTORY_LOGS, DIRECTORY_RETORNOS


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


def plot_time(directory: list = [], **kwargs) -> str:
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
    return_new_data = tm.new_data_frame(directory=directory)
    #tm.filters(columns_interval=['10/05/2020', '25/05/2020'], columns_days=['Segunda'],
    #           index_interval=['08:00:00', '23:30:00'])
    tm.filters()
    tm.extract_values()
    #data = tm.filter_activities(['Dev', 'TCC', 'Trabalho', 'Dormi', 'Outros', 'Descanso', 'Faculdade'])
    data = tm.filter_activities()
    tm.plotar(data=data, type=['all'])
    return_json = return_new_data
    return return_json


def main():
    logging.basicConfig(filename=DIRECTORY_LOGS+datetime.today().strftime("%Y-%m-%d") + '.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

    logging.info('---Iniciado---')

    # netflix(type_plot=True, type_scatter=True)
    # netflix()

    csvs = ['arquivos_testes/Historico_tempo_22 - Página1.csv', 'arquivos_testes/Historico_tempo_23 - Página1.csv',
            'arquivos_testes/Historico_tempo_20 - Página1.csv', 'arquivos_testes/Historico_tempo_21 - Página1.csv',
            'arquivos_testes/Historico_tempo_24 - Página1.csv', 'arquivos_testes/Historico_tempo_25 - Página1.csv',
            'arquivos_testes/Historico_tempo_26 - Página1.csv']
    retorno = plot_time(directory=csvs)

    print(retorno)
    with open(DIRECTORY_RETORNOS + datetime.today().strftime("%Y-%m-%d_%H-%M") + '.json', 'w') as json_file:
        json.dump(retorno, json_file, indent=4, ensure_ascii=False)
        logging.info(f'Arquivo {DIRECTORY_RETORNOS + datetime.today().strftime("%Y-%m-%d_%H-%M")}.json salvo!')

    logging.info('---Finalizado---')

if __name__ == '__main__':
    main()
