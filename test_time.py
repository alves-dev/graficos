import pandas as pd


def upload_csv(directory: list = ['Historico_tempo_21 - Página1.csv', 'Historico_tempo_22 - Página1.csv']) -> list:
    """
    Carrega os dados do csv baixado no google

    :param directory: Lista com os caminhos onde os arquivos se encontram
    :return: Uma lista com os dados
    """
    datas = []
    for i in directory:
        data = open(i).readlines()
        datas.append(data)
    return datas


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

'''
data = upload_csv()
print(data)
'''

dados20 = pd.read_csv('Historico_tempo_20 - Página1.csv')
dados22 = pd.read_csv('Historico_tempo_22 - Página1.csv')
dados23 = pd.read_csv('Historico_tempo_23 - Página1.csv')
unificado = pd.merge(dados20, dados22, left_index=False, right_index=False)
unificado = pd.merge(unificado, dados23, left_index=False, right_index=False)
#print(unificado.index)

#print(f'unificado: {unificado} \n type dados: {type(dados22)}\n  type: {type(unificado)}')
columns20 = dados20.columns.values
columns23 = dados23.columns.values


index = list(unificado['Index'])
print(index)

unificado = unificado.drop(columns=['Index'])
columns_unificados = unificado.columns.values
#print(unificado[columns_unificados])

'''
print(columns20)
print(columns22)
print(columns_unificados)
print(unificado.shape)
'''

arq = open('uni.txt', mode='w')
arq.write(unificado[columns_unificados].to_string())
arq.close

#print(dados[['24/05/2020', '27/05/2020']])
#print(dados[['24/05/2020', 'Unnamed: 1', '27/05/2020', 'Unnamed: 3']])
#print(dados20.loc[0:, columns])

#print(unificado.loc[unificado['10/05/2020'] == 'Domingo', ['10/05/2020', 'Unnamed: 1']])
#print(unificado.loc[lambda d: d['10/05/2020'] == 'Domingo',:])
'''
domingos = ['10/05/2020', '24/05/2020']
print(unificado.loc[0:, lambda d: domingos])
'''
