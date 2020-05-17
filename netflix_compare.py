import matplotlib.pyplot as plt

dados = open("NetflixViewingHistory.csv").readlines()

datas = []
qtd_data = []

########################################################################
for i in dados:
    if i != 'Title,Date\n':
        linha = i.split('",')
        data = linha[1][4:11]
        datas.append(data)

datas.reverse()
########################################################################

cont = 0
ultima_data = ''
intereitor = 0
for i in datas:
    if i != ultima_data:
        if cont > 0:
            qtd_data.append({'data': ultima_data, 'quantidade': cont})
            cont = 0
        ultima_data = i
    cont += 1
    intereitor += 1
    if intereitor == len(datas):
        qtd_data.append({'data': ultima_data, 'quantidade': cont})
########################################################################

anos = []
for i in qtd_data:
    ano = i['data'][3:]
    if ano not in anos:
        anos.append(ano)

anos_dic = {}
for i in anos:
    anos_dic.update({i: {'x': [], 'y': []}})

print(f'pri {anos_dic}')
########################################################################

eixoX = []
eixoY = []

ultima_data = ''
intereitor = 0

def xy(x, y, ano):
    anos_dic[ano]['x'] = x
    anos_dic[ano]['y'] = y
    print(anos_dic[ano])
    val = adiciona_mes(x, y)
    x = val[0]
    y = val[1]
    x = muda_mes_nome(x)
    #plt.hlines(y, 0, 11, linestyles='dashed')
    #plt.vlines(x, 0, y, linestyles='dashed')
    plt.plot(x, y, label=ano)
    plt.scatter(x, y)
    #plt.stem(x,y)

def muda_mes_nome(x):
    messes = ['janeiro', 'fevereiro', 'março', 'abriu', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
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

def adiciona_mes(x, y):
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


for i in qtd_data:
    if i['data'][3:] != ultima_data:
        if ultima_data != '':
            xy(eixoX, eixoY, ultima_data)
        ultima_data = i['data'][3:]

        eixoX.clear()
        eixoY.clear()
    eixoX.append(i['data'][:2])
    eixoY.append(i['quantidade'])

    intereitor += 1
    if intereitor == len(qtd_data):

        xy(eixoX, eixoY, i['data'][3:])

########################################################################

'''
plt.plot(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 168, 102], label='2017')
plt.plot(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'], [49, 78, 42, 79, 93, 80, 108, 65, 33, 71, 114, 133], label='2018')
plt.plot(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'], [120, 53, 87, 73, 56, 110, 49, 109, 109, 130, 89, 98], label='2019')
plt.plot(['01', '02', '03', '04'], [78, 74, 75, 51], label='2020')

plt.scatter(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 168, 102], label='2017')
plt.scatter(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'], [49, 78, 42, 79, 93, 80, 108, 65, 33, 71, 114, 133], label='2018')
plt.scatter(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'], [120, 53, 87, 73, 56, 110, 49, 109, 109, 130, 89, 98], label='2019')
plt.scatter(['01', '02', '03', '04'], [78, 74, 75, 51], label='2020')


#plt.plot(['11/2017', '11/2018', '11/2019', '12/2017', '12/2018', '12/2019'], [168, 114, 89, 102, 133, 98])
plt.plot([11/2017, 14], [168, 102], label='2017')
plt.plot([12/2018, 15], [114, 133], label='2018')
plt.plot([13/2019, 16], [89, 98], label='2019')
'''


#plt.box(on=False)
plt.legend()
plt.title('Quantidade de titulos Netflix')
plt.xlabel('mês/ano')
plt.ylabel('Quantidade de Titulos')

print(anos_dic)

plt.show()

