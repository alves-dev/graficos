from typing import Union, Tuple
from matplotlib import pyplot as plt
import logging
from utility import ReturnJson
from rules import netflix_rules as nr
from graphics import GraphicNetflix


class Netflix:
    def __init__(self, graphic_netflix: GraphicNetflix):
        self.years_dic = {}
        self.re_json = ReturnJson()
        self.graphic_netflix = graphic_netflix

    def plot(self) -> Union[bool, dict]:
        """
        Realiza a plotagem de acordo com os parametros

        :return: escrever aqui....
        """
        valid = nr.type_graphic_valid(self.graphic_netflix.type_graphic)
        if not valid:
            return False

        data = self.upload_csv()

        datas = self.dates_organization(data)
        amount_date = self.count_date(datas)

        if self.graphic_netflix.type_graphic == 'bars':
            self.re_json.add_json('type_graphic', 'bars')
            logging.info(f'plot: Plotando grafico do tipo bars')
            eixoX, eixoY = self.populace_xy_bars(amount_date)
            plt.bar(eixoX, eixoY)
        else:
            self.re_json.add_json('type_graphic', 'compare')
            logging.info(f'plot: Plotando grafico do tipo compare')
            self.years(amount_date)
            self.separates_axes_year(amount_date)

        plt.xticks(rotation=self.graphic_netflix.label_rotation_x)

        plt.title(self.graphic_netflix.title)

        plt.xlabel(self.graphic_netflix.label_axisx)

        plt.ylabel(self.graphic_netflix.label_axisy)

        plt.box(self.graphic_netflix.box)

        plt.legend()
        figure = plt.gcf()
        figure.set_size_inches(12, 8)
        name = self.graphic_netflix.return_name_graphic('netflix')
        plt.savefig(name)
        # plt.show()
        self.re_json.add_json('plotado', name)
        self.re_json.save_json()
        return self.re_json.get_json_dict()

    def upload_csv(self) -> Union[bool, list]:
        """
        Carrega os dados do csv disponibilizado pela netflix

        :return: Uma lista com os dados
        """

        directory = self.graphic_netflix.directory

        valid = nr.valid_archive_upload(directory)
        if not valid:
            return False

        data = open(directory).readlines()
        logging.info(f'upload_csv: Arquivo lido {directory}')
        self.re_json.add_json('processado', directory)
        return data

    def dates_organization(self, data: list) -> list:
        """
        Retira o dia da data deixando assim apenas o mẽs e ano, e reverte a ordem dos dados do mais antigo para o
        mais novo

        :param data: Dados do netflix
        :return: Lista com datas ajustadas
        """
        datas = []

        for i in data:
            if i != 'Title,Date\n':
                line = i.split('",')
                date = line[1][4:11]
                datas.append(date)

        datas.reverse()
        logging.info(f'dates_organization: Retirado o dia da data, ficando mes e ano')
        return datas

    def count_date(self, datas: list) -> list:
        """
        Realiza a contagem de titulos por mês

        :param datas: Dados do netflix
        :return: Retorna uma lista de dicionarios contendo a data e a quantidade respectiva
        """
        amount_date = []

        cont = 0
        last_date = ''
        intereitor = 0
        for i in datas:
            if i != last_date:
                if cont > 0:
                    amount_date.append({'date': last_date, 'amount': cont})
                    cont = 0
                last_date = i
            cont += 1
            intereitor += 1
            if intereitor == len(datas):
                amount_date.append({'date': last_date, 'amount': cont})
        logging.info(f'count_date: Realizado a contagem de titulos por mes')
        return amount_date

    def populace_xy_bars(self, amount_date: list) -> Tuple[list, list]:
        """
        Popula o eixo x e y

        :param amount_date: Contagem de titulos por data
        :return: duas lista eixos x e y
        """
        axisX = []
        axisY = []

        for i in amount_date:
            axisX.append(i['date'])
            axisY.append(i['amount'])
        logging.info(f'populace_xy_bars: Eixos X e Y foram populados com os valores, para bars')
        return axisX, axisY

    def years(self, datas: list) -> dict:
        """
        Recebe a lista de dados e retorna um dicionario contendo o ano e os eixos como uma lista

        :param datas: Quantidade por data
        :return: um dicionario contendo o ano com o valor outro dicionario contendo o eixo x e y;
         {ano: {'x': [], 'y': []}}
        """
        years = []
        for i in datas:
            year = i['date'][3:]
            if year not in years:
                years.append(year)

        for i in years:
            self.years_dic.update({i: {'x': [], 'y': []}})
        logging.info(f'years: Dicionario criado com o "ano" como chave')
        return self.years_dic

    def separates_axes_year(self, datas: list):
        """
        Recebe a lista de dados e separa os eixos x e y por ano

        :param datas: Quantidade por data
        :return: um dicionario contendo o ano com o valor outro dicionario contendo o eixo x e y; {ano: {'x': [], 'y': []}}
        """
        logging.info(f'separates_axes_year: Separando os eixos por ano')
        axisX = []
        axisY = []

        last_date = ''
        intereitor = 0

        for i in datas:
            if i['date'][3:] != last_date:
                if last_date != '':
                    self.assigns_axes_years(axisX, axisY, last_date)
                last_date = i['date'][3:]

                axisX.clear()
                axisY.clear()
            axisX.append(i['date'][:2])
            axisY.append(i['amount'])

            intereitor += 1
            if intereitor == len(datas):
                self.assigns_axes_years(axisX, axisY, i['date'][3:])

    def assigns_axes_years(self, x: list, y: list, year: str):
        """
        Atribui o eixo x e y para o ano certo do dicionario de anos

        :param x: Uma lista para o eixo x
        :param y: Uma lista para o eixo y
        :param year: o ano referente aos valores de x e y
        :return:
        """
        logging.info(f'assigns_axes_years: Plotando o ano {year}')
        self.years_dic[year]['x'] = x
        self.years_dic[year]['y'] = y

        val = self.add_month(x, y)
        x = val[0]
        y = val[1]
        x = self.alter_month_name(x)
        # plt.hlines(y, 0, 11, linestyles='dashed')
        # plt.vlines(x, 0, y, linestyles='dashed')

        list_types = []
        no_type = True

        if self.graphic_netflix.type_plot:
            logging.info(f'assigns_axes_years: type_plot sera aplicado')
            plt.plot(x, y, label=year)
            no_type = False
            list_types.append('type_plot')

        if self.graphic_netflix.type_scatter:
            logging.info(f'assigns_axes_years: type_scatter sera aplicado')
            if no_type:
                plt.scatter(x, y, label=year)
            else:
                plt.scatter(x, y)
            no_type = False
            list_types.append('type_scatter')

        if self.graphic_netflix.type_stem:
            logging.info(f'assigns_axes_years: type_stem sera aplicado')
            plt.stem(x, y)
            no_type = False
            list_types.append('type_stem')

        if no_type:
            logging.info(f'assigns_axes_years: Não definido o tipo; padrao sera aplicado')
            plt.plot(x, y, label=year)
            plt.scatter(x, y)
            list_types.append('type_plot')
            list_types.append('type_scatter')

        self.re_json.add_json('types', list_types)

    def add_month(self, x: list, y: list) -> list:
        """
        Adiciona valores ao x e y para os messes faltantes do ano

        :param x: axis x
        :param y: axis y
        :return: retorna x e y completos com 12 posições
        """
        m = x[0]
        diferenca = int(m) - 1
        i = 1
        x_completo = []
        while i <= diferenca:
            x_completo.append(i)
            i += 1

        for ii in x:
            x_completo.append(ii)

        i = 1
        y_completo = []
        while i <= diferenca:
            y_completo.append(0)
            i += 1

        for ii in y:
            y_completo.append(ii)
        logging.info('add_month: Adicionado os messes faltantes do csv para ficar o ano completo com 12 messes')
        return [x_completo, y_completo]

    def alter_month_name(self, x: list) -> list:
        """
        Altera os messes de numeros para strings

        :param x: lista de messes
        :return: lista de messes em string
        """
        messes = ['Janeiro', 'Fevereiro', 'Março', 'Abriu', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
                  'Novembro', 'Dezembro']
        x_nomes = []

        x = [int(val) for val in x]

        x_nomes.append(messes[0])

        x_nomes.append(messes[1]) if len(x) > 1 else None

        x_nomes.append(messes[2]) if len(x) > 2 else None

        x_nomes.append(messes[3]) if len(x) > 3 else None

        x_nomes.append(messes[4]) if len(x) > 4 else None

        x_nomes.append(messes[5]) if len(x) > 5 else None

        x_nomes.append(messes[6]) if len(x) > 6 else None

        x_nomes.append(messes[7]) if len(x) > 7 else None

        x_nomes.append(messes[8]) if len(x) > 8 else None

        x_nomes.append(messes[9]) if len(x) > 9 else None

        x_nomes.append(messes[10]) if len(x) > 10 else None

        x_nomes.append(messes[11]) if len(x) > 11 else None

        logging.info('alter_month_name: Alterado os números dos messes para os nomes')
        return x_nomes
