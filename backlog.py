# -*- coding: <UTF-8> -*-
import matplotlib.pyplot as plt

dados = open("backlog102019.csv").readlines()

data = []
aberto = []
fechado = []
backlog = []

for i in range(3, len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        dia = linha[0].split("/")
        data.append(int(dia[0]))
        aberto.append(int(linha[1]))
        fechado.append(int(linha[2]))
        backlog.append(int(linha[3]))

plt.title("NewGen - " + dados[0].replace(";", " "))
plt.xlabel("Dia / Mês")
plt.ylabel("Número de chamados")


plt.plot(data, aberto, color="g", label="Abertos")
plt.plot(data, fechado, color="b", label="Fechados")
plt.plot(data, backlog, color="r", label="Backlog")
plt.scatter(data, aberto, color="g")
plt.scatter(data, fechado, color="b")
plt.scatter(data, backlog, color="r")
#plt.plot(x,y, color="k", linestyle="--")
plt.axis([0, 30, 0, 60])
plt.figlegend()
plt.show()

#plt.savefig("pdf.pdf")
#plt.savefig("png.png", dpi=300)