import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime as dt
import logging
from rules import time_rules as tr
from utils import ReturnJson
from graphics import GraphicTime


class DataFrame:
    def __init__(self, graphic_time: GraphicTime):
        self.data_time = None
        self.data_time_filtered = None
        self.values_extract = None
        self.activities_extract = None
        self.re_json = ReturnJson()
        self.graphic_time = graphic_time

    def new_data_frame(self) -> None:
        """
        Seta a variável data_time com os dados dos csv passado como parametro

        :return: None
        """
        logging.info('new_data_frame: Criando um data frame com os CSV')
        self.upload_csv()
        self.rename_index()
        self.order_columns()
        self.alter_nan()
        logging.info('new_data_frame: Data frame criado')

    def plotar(self, data: list) -> dict:
        types = self.graphic_time.type_graphic
        activities_value = {}
        labels = []
        sizes = []
        for i in data:
            temp = (list(i.values())[0])
            o = 0
            while o < len(list(temp.keys())):
                if list(temp.keys())[o] in list(activities_value.keys()):
                    activities_value[list(temp.keys())[o]] = list(temp.values())[o] + activities_value[
                        list(temp.keys())[o]]
                else:
                    activities_value[list(temp.keys())[o]] = list(temp.values())[o]
                o += 1

        o = 0
        while o < len(list(activities_value.keys())):
            labels.append(list(activities_value.keys())[o])
            sizes.append(list(activities_value.values())[o])
            o += 1
        logging.info('plotar: Criada a lista de labels e valores para a plotagem a partir do parametro data')

        list_return = []
        if 'pie' in types or 'all' in types:
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax.set_ylabel('% em relação as atividades filtradas')
            ax.set_title(self.graphic_time.title)
            plt.legend()
            figure = plt.gcf()
            figure.set_size_inches(12, 8)
            name = self.graphic_time.return_name_graphic('pie')
            plt.savefig(name)
            logging.info(f'plotar: Grafico pie plotado e salvo em {name}')
            # plt.show()
            list_return.append({'pie': name})

        if 'bar' in types or 'all' in types:
            fig, ax = plt.subplots()
            r = ax.bar(labels, sizes)
            self.auto_label(r, ax)
            ax.set_ylabel(self.graphic_time.label_axisy)
            ax.set_title(self.graphic_time.title)
            ax.set_xticks(labels)
            ax.set_xticklabels(labels)
            plt.legend()
            figure = plt.gcf()
            figure.set_size_inches(12, 8)
            name = self.graphic_time.return_name_graphic('bar')
            plt.savefig(name)
            logging.info(f'plotar: Grafico bar plotado e salvo em {name}')
            # plt.show()
            list_return.append({'bar': name})

        if 'stem' in types or 'all' in types:
            fig, ax = plt.subplots()
            ax.stem(labels, sizes)
            ax.legend()
            ax.set_ylabel(self.graphic_time.label_axisy)
            ax.set_title(self.graphic_time.title)
            figure = plt.gcf()
            figure.set_size_inches(12, 8)
            name = self.graphic_time.return_name_graphic('stem')
            plt.savefig(name)
            logging.info(f'plotar: Grafico stem plotado e salvo em {name}')
            # plt.show()
            list_return.append({'stem': name})

        if 'scatter' in types or 'all' in types:
            name = self.plot_scatter(data)
            list_return.append({'scatter': name})

        self.re_json.add_json('plotado', list_return)
        self.re_json.save_json()
        return self.re_json.get_json_dict()

    def plot_scatter(self, data) -> str:

        fig, ax = plt.subplots()

        labels = []
        sizes = []
        for act in self.activities_extract:
            for i in data:
                labels.append(list(i.keys())[0])
                temp = (list(i.values())[0])
                val = 0
                if act in list(temp.keys()):
                    val = temp[act]
                sizes.append(val)
            ax.plot(labels, sizes, label=act)
            ax.scatter(labels, sizes)

            labels = []
            sizes = []

        ax.set_ylabel(self.graphic_time.label_axisy)
        ax.set_title(self.graphic_time.title)
        plt.xticks(rotation=self.graphic_time.label_rotation_x)
        plt.legend()
        figure = plt.gcf()
        figure.set_size_inches(12, 8)
        name = self.graphic_time.return_name_graphic('scatter')
        plt.savefig(name)
        logging.info(f'plotar: Grafico scatter plotado e salvo em {name}')
        # plt.show()
        return name

    def auto_label(self, rects, ax):
        """
        anexe um rótulo de texto acima de cada barra em * react *, exibindo sua altura
        """
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    def upload_csv(self) -> bool:
        """
        Carrega os dados dos CSVs, e unifica todos em um só data frame

        :return: None
        """
        directory = self.graphic_time.directory
        logging.info(f'upload_csv: Lendo arquivos CSV={directory}')

        valid = tr.valid_archive_upload(directory)
        if not valid:
            return False

        unificado = pd.read_csv(directory[1])

        for i in directory:
            data = pd.read_csv(i)
            unificado = pd.merge(data, unificado, left_index=False, right_index=False)

        self.data_time = unificado.drop(columns=['Index'])
        logging.info('upload_csv: CSVs lidos e unificados em um unico data frame')

        self.re_json.add_json('processados', directory)

    def rename_index(self) -> None:
        """
        Renomeia os index do data frame, de 0 a 48 por 00:00:00 até 23:30:00

        :return: None
        """

        self.data_time = self.data_time.rename(
            {0: 'nan', 1: '00:00:00', 2: '00:30:00', 3: '01:00:00', 4: '01:30:00', 5: '02:00:00',
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

    def order_columns(self) -> None:
        """
        Reordena as colunas em ordem, para isso é criado uma lista convertendo str em date, então a lista é ordenada e
        depois é convertida de volta para str, podendo setar a variável data_time com as colunas ordenadas

        :return: None
        """
        logging.info('order_columns: Iniciando ordenação de colunas por data')

        dates = list(self.data_time.columns.values)

        date_formated = []
        for i in dates:
            d = dt.strptime(i, '%d/%m/%Y').date()
            date_formated.append(d)

        date_formated = sorted(date_formated)

        dates_br_ordered = []
        for i in date_formated:
            d = i.strftime('%d/%m/%Y')
            dates_br_ordered.append(d)

        self.data_time = self.data_time[dates_br_ordered]
        logging.info('order_columns: Fim da ordenação de colunas')

    def alter_nan(self) -> None:
        """
        Substitui o valor nan do pandas por null para ficar padrão com o CSV

        :return: None
        """
        self.data_time = self.data_time.fillna('null', inplace=False)
        logging.info('alter_nan: Alterados os valores nan por null')

    def filters(self) -> None:
        """
        Realiza o filtro no data frame de acordo com os parametros,
        e atribui o valor filtrado a variável data_time_filtered.

        :return: None
        """
        logging.info('filters: Iniciando o filtramento no data frame')

        if len(self.graphic_time.columns_days) == 0:
            self.del_index_days()

        self.data_time_filtered = self.data_time

        list_return = []
        if len(self.graphic_time.index_interval) > 0:
            logging.info(f'filters : index_interval {self.graphic_time.index_interval[0]} até '
                         f'{self.graphic_time.index_interval[1]}')
            self.data_time_filtered = self.data_time_filtered.loc[self.graphic_time.index_interval[0]:
                                                                  self.graphic_time.index_interval[1],
                                      list(self.data_time.columns.values)]
            list_return.append('index_interval')

        if len(self.graphic_time.index) > 0:
            logging.info(f'filters : index {self.graphic_time.index}')
            self.data_time_filtered = self.data_time_filtered.loc[self.graphic_time.index,
                                                                  list(self.data_time.columns.values)]
            list_return.append('index')

        if len(self.graphic_time.columns_interval) > 0:
            logging.info(f'filters : columns_interval {self.graphic_time.columns_interval[0]} até '
                         f'{self.graphic_time.columns_interval[1]}')
            self.data_time_filtered = self.data_time_filtered.loc[:, self.graphic_time.columns_interval[0]:
                                                                     self.graphic_time.columns_interval[1]]
            list_return.append('columns_interval')

        if len(self.graphic_time.columns) > 0:
            logging.info(f'filters: columns {self.graphic_time.columns}')
            self.data_time_filtered = self.data_time_filtered[self.graphic_time.columns]
            list_return.append('columns')

        if len(self.graphic_time.columns_days) > 0:
            logging.info(f'filters : columns_days {self.graphic_time.columns_days}')
            self.data_time_filtered = self.data_time_filtered[self.list_days(self.graphic_time.columns_days)]
            list_return.append('columns_days')

        logging.info('filters: Fim do filtramento no data frame')

        self.re_json.add_json('filters', list_return)

    def list_days(self, days) -> list:
        """
        Filtra as datas de acordo com os dias da semana

        :param days: Uma lista de dias da semana, exemplo=['Segunda', 'Quinta']
        :return: Retorna uma lista contendo as datas referente aos dias da semana
        """
        logging.info(f'list_days: Listando datas pelos dias da semana: {days}')

        temp = self.data_time.loc[['nan']].to_dict()

        days_list = []
        for i in temp:
            days_list.append({i: temp[i]["nan"]})

        list_columns = []
        for i in days_list:
            if list(i.values())[0] in days:
                list_columns.append(list(i.keys())[0])

        columns_data_time_filtered = list(self.data_time_filtered.columns.values)
        list_columns_filtered = []
        for i in list_columns:
            if i in columns_data_time_filtered:
                list_columns_filtered.append(i)

        logging.info(f'list_days: Datas listadas: {list_columns_filtered}')
        return list_columns_filtered

    def del_index_days(self) -> None:
        """
        Deleta o index nan, que é a linha que consta o nome dos dias da semana

        :return: None
        """

        self.data_time = self.data_time.drop('nan')
        logging.info('del_index_days: Index nan deletado')

    def extract_values(self) -> None:
        """
        Atribui a variável values_extract os valores extraidos do data_time_filtered

        :return: Uma lista de dicionarios contendo a quantidade de cada atividade por dia,
        exemplo= [{'13/05/2020': {'Trabalho': 17}}, {'14/05/2020': {'Dev': 2, 'Trabalho': 21}}]
        """

        # TODO Em caso de ser filtrado apenas uma coluna esse metodo ira dar um erro, VERIFICAR
        columns = list(self.data_time_filtered.columns.values)
        index_c = len(columns) - 1
        values = []
        for i in columns:
            df = self.data_time_filtered.groupby(i).count()
            dict_value = {i: dict(df[columns[index_c]])}
            index_c = 0
            values.append(dict_value)

        self.values_extract = values
        logging.info(f'extract_values: Extraido os valores do data frame, valores={values}')

    def filter_activities(self) -> list:
        """
        Filtra as atividades passada como parametro na variável values_extract

        :return: Uma lista de dicionarios contendo a quantidade de cada atividade por dia,
        exemplo= [{'13/05/2020': {'Trabalho': 17}}, {'14/05/2020': {'Dev': 2, 'Trabalho': 21}}]
        """
        logging.info(f'filter_activities: Iniciando o filtro das atividades: {self.graphic_time.activities}')
        self.activities_extract = activities = self.graphic_time.activities

        activities_filtered = []
        empty = False
        if len(activities) == 0:
            empty = True
            self.activities_extract = []

        for i in self.values_extract:
            v = list(i.values())[0]
            dict_temp = {list(i.keys())[0]: {}}
            sub_dict_temp = {}

            if empty:
                activities = v

            for act in activities:
                if act not in self.activities_extract:
                    self.activities_extract.append(act)

                if act in v:
                    sub_dict_temp[act] = v[act]
                dict_temp[list(i.keys())[0]] = sub_dict_temp

            if len(sub_dict_temp) > 0:
                activities_filtered.append(dict_temp)

        self.re_json.add_json('filter_activities', self.activities_extract)
        logging.info(f'filter_activities: Fim do filtro das atividades, valores retornados: {activities_filtered}')
        return activities_filtered
