import matplotlib.pyplot as plt



x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 7, 3]

# cria uma linha de x,y até xd,yd
#plt.arrow(1, 1, 5, 7)


# cria uma anotação na posição (x, y)
#plt.annotate('anotação', (3, 5))
# cria uma anotação na posição xytext=(x, y), e faz uma seta para (1, 1)
#plt.annotate('anotação', (1, 1), xytext=(1, 7), arrowprops={})


# faz uma linha na horizontal na posição y, pode ser usado como medida de meta
#plt.axhline(y=3, color='r')
# faz uma linha na vertical na posição x,
#plt.axvline(x=3)


# retira as linhas da caixa
#plt.box(on=False)

# Ler sobre https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.connect.html#matplotlib.pyplot.connect
#plt.connect()

# Traçar linhas horizontais/ verticais em cada y de xmin a xmax .
# plt.vlines(x, 0, y, linestyles='dashed')


# grafico de pizza:
'''
labels = ['janeiro', 'fevereiro', 'março', 'abriu', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
sizes = [15, 30, 45, 10, 30, 45, 10, 30, 45, 10, 30, 45]
explode = (0, 0, 0, 0, 0.2, 0.0, 0, 0.0, 0.0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
'''

# adiciona o texto na coordenada
#plt.text(2, 2, 'text')

#substitui os labels do eixo x
text = ['um', 'dois', 'tres', 'quatro', 'cinco']
plt.xticks(x, text)

# Documentação para mais exemplos
# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.html

#plota linhas verticais de uma linha de base até a coordenada y e coloca um marcador na ponta.
#plt.stem(x, y)



plt.bar(x, y)
plt.title('titulo')
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.legend()

plt.show()

