# -*- coding: <UTF-8> -*-
import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.title("Crescimento da pupulação")
plt.xlabel("Ano")
plt.ylabel("Pulação x100.000.000")


plt.bar(x,y, color="#e4e4e4")
plt.plot(x,y, color="k", linestyle="--")
plt.show()
#plt.savefig("pdf.pdf")
#plt.savefig("png.png", dpi=300)
