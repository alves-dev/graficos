import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime as dt
import logging
import numpy as np

global data_time


def new_data_frame(directory: list, **kwargs):
    logging.info('New data frame')
    global data_time
    upload_csv(directory=directory)
    rename_index()
    order_columns()
    alter_nan()

    #print(list(data_time.index.values))
    #print(list(data_time.columns.values))
    print(data_time.head())


def plotar():
    global data_time

    #filters(index=['04:30:00', '07:30:00'], columns_interval=['10/05/2020', '15/05/2020'])
    #filters(index=['04:30:00', '07:30:00'], columns_days=['Domingo', 'Segunda'])
    filters()



def upload_csv(directory: list) -> object:
    """
    Carrega os dados do csv

    :param directory: Lista com os caminhos onde os arquivos se encontram
    :return:
    """
    unificado = pd.read_csv(directory[1])

    for i in directory:
        data = pd.read_csv(i)
        unificado = pd.merge(data, unificado, left_index=False, right_index=False)
    global data_time
    data_time = unificado.drop(columns=['Index'])


def rename_index():
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


def order_columns():
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


def alter_nan():
    global data_time
    data_time = data_time.fillna('null', inplace=False)


def filters(index: list = None, index_interval: list = None, columns: list = None, columns_days: list = None,
            columns_interval: list = None):
    global data_time
    if columns_days is None:
        del_index_days()

    filtrado = data_time

    if index is not None:
        logging.info(f'filters : index {index}')
        print('index')
        filtrado = filtrado.loc[index, list(data_time.columns.values)]

    if index_interval is not None:
        logging.info(f'filters : index_interval {index_interval[0]} até {index_interval[1]}')
        print('index_interval')
        filtrado = filtrado.loc[index_interval[0]: index_interval[1], list(data_time.columns.values)]

    if columns is not None:
        logging.info(f'filters: columns {columns}')
        print('columns')
        filtrado = filtrado[columns]

    if columns_interval is not None:
        logging.info(f'filters : columns_interval {columns_interval[0]} até {columns_interval[1]}')
        print(f'columns_interval {columns_interval[0]} e {columns_interval[1]}')
        filtrado = filtrado.loc[:, columns_interval[0]: columns_interval[1]]

    if columns_days is not None:
        logging.info(f'filters : columns_days {columns_days}')
        print('columns_days')
        list_days(columns_days)
        filtrado = filtrado[list_days(columns_days)]

    print(filtrado.head())
    data_time = filtrado


def list_days(lista_p) -> list:
    global data_time
    lista = dict(data_time.loc[['nan']])
    d = data_time.loc[['nan']].to_dict()
    #print(data_time.loc[['nan']])
    #print(lista)
    #print(d)

    days_list = []
    #print('DIASSSSS')
    for i in d:
        #print(f'{i} : {d[i]["nan"]}')
        days_list.append({i:d[i]["nan"]})

    list_columns = []
    for i in days_list:
        print(list(i.values())[0])
        if list(i.values())[0] in lista_p:
            print(list(i.keys())[0])
            list_columns.append(list(i.keys())[0])

    return list_columns


def del_index_days():
    global data_time
    data_time = data_time.drop('nan')
