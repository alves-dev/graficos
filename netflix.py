import matplotlib.pyplot as plt
import os.path

global years_dic

def plot(type_graphic: str, **kwargs) -> object:
    """
    Realiza a plotagem de acordo com os parametros

    :param kwargs:
        :key directory: caminho do csv da netflix
        :key title: titulo do grafico
        :key label_axisx: texto do eixo x
        :key label_axisy: texto do eixo y
        :key label_rotation_x: rotação do texto eixo x, valores {ângulo em graus, 'vertical', 'horizontal'}
        :key box: True ou False para caixa do grafico
    :return:
    """

    if 'directory' in kwargs and os.path.exists(kwargs.get('directory')):
        data = upload_csv(kwargs.get('directory'))
    else:
        data = upload_csv()

    datas = dates_organization(data)
    amount_date = count_date(datas)

    if type_graphic == 'bars':
        eixoX, eixoY = populace_xy_bars(amount_date)
        plt.bar(eixoX, eixoY)
    else:
        print('tipode grafico compare ou invalido por isso o compare')
        years(amount_date)
        separates_axes_year(amount_date, **kwargs)



    if 'label_rotation_x' in kwargs:
        plt.xticks(rotation=kwargs.get('label_rotation_x'))

    if 'title' in kwargs:
        plt.title(kwargs.get('title'))
    else:
        plt.title('Quantidade de titulos Netflix')

    if 'label_axisx' in kwargs:
        plt.xlabel(kwargs.get('label_axisx'))
    else:
        plt.xlabel('mês/ano')

    if 'label_axisy' in kwargs:
        plt.ylabel(kwargs.get('label_axisy'))
    else:
        plt.ylabel('Quantidade de Titulos')

    if 'box' in kwargs:
        plt.box(on=kwargs.get('box'))
    else:
        plt.box(on=True)

    plt.legend()
    plt.show()
    return True


def upload_csv(directory: str = 'NetflixViewingHistory.csv') -> list:
    """
    Carrega os dados do csv disponibilizado pela netflix

    :param directory: Caminho onde o arquivo se encontra
    :return: Uma lista com os dados
    """
    data = open(directory).readlines()
    return data


def dates_organization(data: list) -> list:
    """
    Retira o dia da data deixando assim apenas o mẽs e ano, e reverte a ordem dos dados do mais antigo para o mais novo

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

    return datas


def count_date(datas: list) -> list:
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

    return amount_date


def populace_xy_bars(amount_date: list) -> list:
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

    return axisX, axisY


def years(datas: list) -> dict:
    """
    Recebe a lista de dados e retorna um dicionario contendo o ano e os eixos como uma lista

    :param datas: Quantidade por data
    :return: um dicionario contendo o ano com o valor outro dicionario contendo o eixo x e y; {ano: {'x': [], 'y': []}}
    """
    years = []
    for i in datas:
        year = i['date'][3:]
        if year not in years:
            years.append(year)
    global years_dic
    years_dic = {}
    for i in years:
        years_dic.update({i: {'x': [], 'y': []}})

    return years_dic


def separates_axes_year(datas: list, **kwargs):
    """
    Recebe a lista de dados e separa os eixos x e y por ano

    :param datas: Quantidade por data
    :return: um dicionario contendo o ano com o valor outro dicionario contendo o eixo x e y; {ano: {'x': [], 'y': []}}
    """

    axisX = []
    axisY = []

    last_date = ''
    intereitor = 0

    for i in datas:
        if i['date'][3:] != last_date:
            if last_date != '':
                assigns_axes_years(axisX, axisY, last_date, **kwargs)
            last_date = i['date'][3:]

            axisX.clear()
            axisY.clear()
        axisX.append(i['date'][:2])
        axisY.append(i['amount'])

        intereitor += 1
        if intereitor == len(datas):
            assigns_axes_years(axisX, axisY, i['date'][3:], **kwargs)


def assigns_axes_years(x: list, y: list, year: str, **kwargs):
    """
    Atribui o eixo x e y para o ano certo do dicionario de anos

    :param x: Uma lista para o eixo x
    :param y: Uma lista para o eixo y
    :param year: o ano referente aos valores de x e y
    :return:
    """

    years_dic[year]['x'] = x
    years_dic[year]['y'] = y
    print(years_dic[year])
    val = add_month(x, y)
    x = val[0]
    y = val[1]
    x = alter_month_name(x)
    # plt.hlines(y, 0, 11, linestyles='dashed')
    # plt.vlines(x, 0, y, linestyles='dashed')

    no_type = True
    if 'type_plot' in kwargs:
        if kwargs.get('type_plot'):
            plt.plot(x, y, label=year)
            no_type = False

    if 'type_scatter' in kwargs:
        if kwargs.get('type_scatter'):
            if no_type:
                plt.scatter(x, y, label=year)
            else:
                plt.scatter(x, y)
            no_type = False

    if 'type_stem' in kwargs:
        if kwargs.get('type_stem'):
            plt.stem(x, y)
            no_type = False

    if no_type:
        print('não definifo o tipo, padrao sera aplixado')
        plt.plot(x, y, label=year)
        plt.scatter(x, y)


def add_month(x: list, y: list) -> list:
    """
    Adiciona valores ao x e y para os messes faltantes do ano

    :param x: axis x
    :param y: axis y
    :return: retorna x e y completos com 12 posições
    """
    m = x[0]
    print(f'mes = {m}')
    diferenca = int(m) - 1
    print(f'diferenca = {diferenca}')
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

    return [x_completo, y_completo]


def alter_month_name(x: list) -> list:
    """
    Altera os messes de numeros para strings

    :param x: lista de messes
    :return: lista de messes em string
    """
    messes = ['Janeiro', 'Fevereiro', 'Março', 'Abriu', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
              'Novembro', 'Dezembro']
    x_nomes = []

    if x[0] == 1 or x[0] == '01':
        x_nomes.append(messes[0])

    if len(x) > 1:
        if x[1] == 2 or x[1] == '02':
            x_nomes.append(messes[1])

    if len(x) > 2:
        if x[2] == 3 or x[2] == '03':
            x_nomes.append(messes[2])

    if len(x) > 3:
        if x[3] == 4 or x[3] == '04':
            x_nomes.append(messes[3])

    if len(x) > 4:
        if x[4] == 5 or x[4] == '05':
            x_nomes.append(messes[4])

    if len(x) > 5:
        if x[5] == 6 or x[5] == '06':
            x_nomes.append(messes[5])

    if len(x) > 6:
        if x[6] == 7 or x[6] == '07':
            x_nomes.append(messes[6])

    if len(x) > 7:
        if x[7] == 8 or x[7] == '08':
            x_nomes.append(messes[7])

    if len(x) > 8:
        if x[8] == 9 or x[8] == '09':
            x_nomes.append(messes[8])

    if len(x) > 9:
        if x[9] == 10 or x[9] == '10':
            x_nomes.append(messes[9])

    if len(x) > 10:
        if x[10] == 11 or x[10] == '11':
            x_nomes.append(messes[10])

    if len(x) > 11:
        if x[11] == 12 or x[11] == '12':
            x_nomes.append(messes[11])

    return x_nomes
