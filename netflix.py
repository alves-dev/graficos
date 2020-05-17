import matplotlib.pyplot as plt
import os.path


def plot_bars(**kwargs) -> object:
    """
    Realiza a plotagem de acordo com os parametros

    :param kwargs:
        :key directory: caminho do csv da netflix
        :key title: titulo do grafico
        :key label_axisx: texto do eixo x
        :key label_axisy: texto do eixo y
        :key label_rotation_x: rotação do texto eixo x, valores {ângulo em graus, 'vertical', 'horizontal'}
    :return:
    """

    if 'directory' in kwargs and os.path.exists(kwargs.get('directory')):
        data = upload_csv(kwargs.get('directory'))
    else:
        data = upload_csv()

    datas = dates_organization(data)
    amount_date = count_date(datas)
    eixoX, eixoY = populace_xy_bars(amount_date)
    plt.bar(eixoX, eixoY)

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

    plt.show()
    return True


def plot_compare(**kwargs) -> object:
    """
    Realiza a plotagem de acordo com os parametros

    :param kwargs:
        :key directory: caminho do csv da netflix
        :key title: titulo do grafico
        :key label_axisx: texto do eixo x
        :key label_axisy: texto do eixo y
        :key label_rotation_x: rotação do texto eixo x, valores {ângulo em graus, 'vertical', 'horizontal'}
    :return:
    """

    if 'directory' in kwargs and os.path.exists(kwargs.get('directory')):
        data = upload_csv(kwargs.get('directory'))
    else:
        data = upload_csv()

    datas = dates_organization(data)
    amount_date = count_date(datas)

    da qui para baixo muda
    eixoX, eixoY = populace_xy_bars(amount_date)
    plt.bar(eixoX, eixoY)

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





