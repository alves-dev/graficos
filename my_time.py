import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime as dt
import logging
from constants import DIRECTORY_PLOTAGENS
from datetime import datetime

global data_time
global data_time_filtered
global values_extract
global activities_extract


def new_data_frame(directory: list) -> dict:
    """
    Seta a variável global data_time com os dados dos csv passado como parametro

    :return: None
    """
    logging.info('new_data_frame: Criando um data frame com os CSV')
    global data_time
    return_upload = upload_csv(directory=directory)
    rename_index()
    order_columns()
    alter_nan()
    logging.info('new_data_frame: Data frame criado')
    return return_upload

def plotar(data: list, type: list = ['all']) -> None:
    print(data)
    activities_value = {}
    labels = []
    sizes = []
    for i in data:
        temp = (list(i.values())[0])
        o = 0
        while o < len(list(temp.keys())):
            if list(temp.keys())[o] in list(activities_value.keys()):
                activities_value[list(temp.keys())[o]] = list(temp.values())[o] + activities_value[list(temp.keys())[o]]
            else:
                activities_value[list(temp.keys())[o]] = list(temp.values())[o]
            o += 1
    print(activities_value)
    o = 0
    while o < len(list(activities_value.keys())):
        labels.append(list(activities_value.keys())[o])
        sizes.append(list(activities_value.values())[o])
        o += 1

    if 'pie' in type or 'all' in type:
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.legend()
        figure = plt.gcf()
        figure.set_size_inches(12, 8)
        plt.savefig(DIRECTORY_PLOTAGENS + datetime.today().strftime("%Y-%m-%d_%H-%M") + '_pie')
        #plt.show()


    if 'bar' in type or 'all' in type:
        fig, ax = plt.subplots()
        r = ax.bar(labels, sizes)
        auto_label(r, ax)
        ax.set_ylabel('Quantidade / 2 = X horas ')
        ax.set_title('Atividades')
        ax.set_xticks(labels)
        ax.set_xticklabels(labels)
        plt.legend()
        figure = plt.gcf()
        figure.set_size_inches(12, 8)
        plt.savefig(DIRECTORY_PLOTAGENS + datetime.today().strftime("%Y-%m-%d_%H-%M") + '_bar')
        #plt.show()

    if 'stem' in type or 'all' in type:
        plt.stem(labels, sizes)
        plt.legend()
        figure = plt.gcf()
        figure.set_size_inches(12, 8)
        plt.savefig(DIRECTORY_PLOTAGENS + datetime.today().strftime("%Y-%m-%d_%H-%M") + '_stem')
        #plt.show()

    if 'scatter' in type or 'all' in type:
        plot_scatter(data)


def plot_scatter(data) -> None:
    global activities_extract
    #lista = ['Dev', 'TCC', 'Trabalho', 'Dormi', 'Outros', 'Descanso',  'Faculdade']
    lista = ['Trabalho', 'Dormi', 'Descanso']
    labels = []
    sizes = []
    for act in activities_extract:
        for i in data:
            labels.append(list(i.keys())[0])
            temp = (list(i.values())[0])
            val = 0
            if act in list(temp.keys()):
                val = temp[act]
            sizes.append(val)
        plt.plot(labels, sizes, label=act)
        plt.scatter(labels, sizes)
        print(f'{labels}, {sizes}, {act}')
        labels = []
        sizes = []

    plt.xticks(rotation='60')
    plt.legend()
    figure = plt.gcf()
    figure.set_size_inches(12, 8)
    plt.savefig(DIRECTORY_PLOTAGENS + datetime.today().strftime("%Y-%m-%d_%H-%M") + '_scatter')
    #plt.show()


def auto_label(rects, ax):
    """anexe um rótulo de texto acima de cada barra em * react *, exibindo sua altura"""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def upload_csv(directory: list) -> dict:
    """
    Carrega os dados dos CSVs, e unifica todos em um só data frame

    :param directory: Lista com os caminhos onde os arquivos se encontram
    :return: None
    """
    logging.info(f'upload_csv: Lendo arquivos CSV={directory}')
    unificado = pd.read_csv(directory[1])

    for i in directory:
        data = pd.read_csv(i)
        unificado = pd.merge(data, unificado, left_index=False, right_index=False)
    global data_time
    data_time = unificado.drop(columns=['Index'])
    logging.info('upload_csv: CSVs lidos e unificados em um unico data frame')
    return {'Processados': directory}


def rename_index() -> None:
    """
    Renomeia os index do data frame, de 0 a 48 por 00:00:00 até 23:30:00

    :return: None
    """
    global data_time
    data_time = data_time.rename({0: 'nan', 1: '00:00:00', 2: '00:30:00', 3: '01:00:00', 4: '01:30:00', 5: '02:00:00',
                                  6: '02:30:00', 7: '03:00:00', 8: '03:30:00', 9: '04:00:00', 10: '04:30:00',
                                  11: '05:00:00', 12: '05:30:00', 13: '06:00:00', 14: '06:30:00', 15: '07:00:00',
                                  16: '07:30:00', 17: '08:00:00', 18: '08:30:00', 19: '09:00:00', 20: '09:30:00',
                                  21: '10:00:00', 22: '10:30:00', 23: '11:00:00', 24: '11:30:00', 25: '12:00:00',
                                  26: '12:30:00', 27: '13:00:00', 28: '13:30:00', 29: '14:00:00', 30: '14:30:00',
                                  31: '15:00:00', 32: '15:30:00', 33: '16:00:00', 34: '16:30:00', 35: '17:00:00',
                                  36: '17:30:00', 37: '18:00:00', 38: '18:30:00', 39: '19:00:00', 40: '19:30:00',
                                  41: '20:00:00', 42: '20:30:00', 43: '21:00:00', 44: '21:30:00', 45: '22:00:00',
                                  46: '22:30:00', 47: '23:00:00', 48: '23:30:00'})
    logging.info('rename_index: Os index foram renomeados')


def order_columns() -> None:
    """
    Reordena as colunas em ordem, para isso é criado uma lista convertendo str em date, então a lista é ordenada e
    depois é convertida de volta para str, podendo setar a variável global data_time com as colunas ordenadas

    :return: None
    """
    logging.info('order_columns: Iniciando ordenação de colunas')
    global data_time

    dates = list(data_time.columns.values)

    date_formated = []
    for i in dates:
        d = dt.strptime(i, '%d/%m/%Y').date()
        date_formated.append(d)

    date_formated = sorted(date_formated)

    dates_br_ordered = []
    for i in date_formated:
        d = i.strftime('%d/%m/%Y')
        dates_br_ordered.append(d)

    data_time = data_time[dates_br_ordered]
    logging.info('order_columns: Fim da ordenação de colunas')


def alter_nan() -> None:
    """
    Substitui o valor nan do pandas por null para ficar padrão com o CSV

    :return: None
    """
    global data_time
    data_time = data_time.fillna('null', inplace=False)
    logging.info('alter_nan: Alterados os valores nan por null')


def filters(index: list = None, index_interval: list = None, columns: list = None, columns_days: list = None,
            columns_interval: list = None) -> None:
    """
    Realiza o filtro no data frame de acordo com os parametros,
    e atribui o valor filtrado a variável global data_time_filtered.

    :param index: uma lista de index para serem filtrado = ['04:30:00', ..., '07:30:00']
    :param index_interval: uma lista de dois index para serem filtrado entre eles = ['08:00:00', '17:30:00']
    :param columns: uma lista de datas para serem filtradas = ['10/05/2020',..., '15/05/2020']
    :param columns_days: uma lista de dias da semana para serem filtrado = ['Segunda','terca','...']
    :param columns_interval: uma lista contendo datas para serem filtradas entre elas= ['22/12/2019','21/02/2020']
    :return: None
    """
    logging.info('filters: Iniciando o filtramento no data frame')
    global data_time
    global data_time_filtered
    if columns_days is None:
        del_index_days()

    data_time_filtered = data_time

    if index_interval is not None:
        logging.info(f'filters : index_interval {index_interval[0]} até {index_interval[1]}')
        data_time_filtered = data_time_filtered.loc[index_interval[0]: index_interval[1], list(data_time.columns.values)]

    if index is not None:
        logging.info(f'filters : index {index}')
        data_time_filtered = data_time_filtered.loc[index, list(data_time.columns.values)]

    if columns_interval is not None:
        logging.info(f'filters : columns_interval {columns_interval[0]} até {columns_interval[1]}')
        data_time_filtered = data_time_filtered.loc[:, columns_interval[0]: columns_interval[1]]

    if columns is not None:
        logging.info(f'filters: columns {columns}')
        data_time_filtered = data_time_filtered[columns]

    if columns_days is not None:
        logging.info(f'filters : columns_days {columns_days}')
        data_time_filtered = data_time_filtered[list_days(columns_days)]

    logging.info('filters: Fim do filtramento no data frame')
    print(data_time_filtered.head())


def list_days(days) -> list:
    """
    Filtra as datas de acordo com os dias da semana

    :param days: Uma lista de dias da semana, exemplo=['Segunda', 'Quinta']
    :return: Retorna uma lista contendo as datas referente aos dias da semana
    """
    logging.info(f'list_days: Listando datas pelos dias da semana: {days}')
    global data_time_filtered
    global data_time
    temp = data_time.loc[['nan']].to_dict()

    days_list = []
    for i in temp:
        days_list.append({i: temp[i]["nan"]})

    list_columns = []
    for i in days_list:
        if list(i.values())[0] in days:
            list_columns.append(list(i.keys())[0])

    columns_data_time_filtered = list(data_time_filtered.columns.values)
    list_columns_filtered = []
    for i in list_columns:
        if i in columns_data_time_filtered:
            list_columns_filtered.append(i)

    logging.info(f'list_days: Datas listadas: {list_columns_filtered}')
    return list_columns_filtered


def del_index_days() -> None:
    """
    Deleta o index nan, que é a linha que consta o nome dos dias da semana

    :return: None
    """
    global data_time
    data_time = data_time.drop('nan')
    logging.info('del_index_days: Index nan deletado')


def extract_values() -> None:
    """
    Atribui a variável global values_extract os valores extraidos do data_time_filtered

    :return: Uma lista de dicionarios contendo a quantidade de cada atividade por dia,
    exemplo= [{'13/05/2020': {'Trabalho': 17}}, {'14/05/2020': {'Dev': 2, 'Trabalho': 21}}]
    """
    global data_time_filtered
    global values_extract
    #TODO Em caso de ser filtrado apenas uma coluna esse metodo ira dar um erro, VERIFICAR
    columns = list(data_time_filtered.columns.values)
    index_c = len(columns)-1
    values = []
    for i in columns:
        df = data_time_filtered.groupby(i).count()
        dict_value = {i: dict(df[columns[index_c]])}
        index_c = 0
        values.append(dict_value)

    values_extract = values
    logging.info(f'extract_values: Extraido os valores do data frame, valores={values}')


def filter_activities(activities: list = None) -> list:
    """
    Filtra as atividades passada como parametro na variável global values_extract

    :param activities: Uma lista de str das atividades, exemplo='Dev', 'null', 'Trabalho']
    :return: Uma lista de dicionarios contendo a quantidade de cada atividade por dia,
    exemplo= [{'13/05/2020': {'Trabalho': 17}}, {'14/05/2020': {'Dev': 2, 'Trabalho': 21}}]
    """
    logging.info(f'filter_activities: Iniciando o filtro das atividades: {activities}')
    global values_extract
    global activities_extract
    activities_extract = activities

    activities_filtered = []
    empty = False
    if activities is None:
        empty = True
        activities_extract = []

    for i in values_extract:
        v = list(i.values())[0]
        dict_temp = {list(i.keys())[0]: {}}
        sub_dict_temp = {}

        if empty:
            activities = v

        for act in activities:
            if act not in activities_extract:
                activities_extract.append(act)

            if act in v:
                sub_dict_temp[act] = v[act]
            dict_temp[list(i.keys())[0]] = sub_dict_temp

        if len(sub_dict_temp) > 0:
            activities_filtered.append(dict_temp)

    logging.info(f'filter_activities: FIm do filtro das atividades, valores retornados: {activities_filtered}')
    return activities_filtered
