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

eixoX = []
eixoY = []

for i in qtd_data:
    eixoX.append(i['data'])
    eixoY.append(i['quantidade'])

########################################################################

plt.bar(eixoX, eixoY)

plt.title('Quantidade de titulos Netflix')
plt.xlabel('mês/ano')
plt.ylabel('Quantidade de Titulos')

print(qtd_data)

plt.show()