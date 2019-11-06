# -*- coding: <UTF-8> -*-
import matplotlib.pyplot as plt

dados = open("backlog102019.csv").readlines()

data = []
aberto = []
fechado = []
backlog = []

fatia = []

for i in range(3, len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        dia = linha[0].split("/")
        data.append(int(dia[0]))
        aberto.append(int(linha[1]))
        fechado.append(int(linha[2]))
        backlog.append(int(linha[3]))
        fatia.clear()
        fatia.append(int(linha[1]))
        fatia.append(int(linha[2]))
        fatia.append(int(linha[3]))

plt.title("NewGen - " + dados[0].replace(";", " "))
plt.xlabel("Dia / Mês")
plt.ylabel("Número de chamados")

nomes = ['aberto', 'fechado', 'backlog']
cores = ['c', 'm', 'r']

plt.pie(fatia, labels=nomes, colors=cores)
plt.figlegend()
plt.show()

#plt.savefig("pdf.pdf")
#plt.savefig("png.png", dpi=300)