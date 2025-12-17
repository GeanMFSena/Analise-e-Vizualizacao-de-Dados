import matplotlib.pyplot as plt

# plt.style.use('seaborn-v0_8')

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25] 

# fig,ax, = plt.subplots()

# ax.scatter(x_values,y_values, s=200)

# ax.set_title('Square Numbers', fontsize = 24)
# ax.set_xlabel('Value', fontsize= 14)
# ax.set_ylabel('Square', fontsize=14)

# ax.tick_params(labelsize=14)

# plt.show()

plt.style.use('seaborn-v0_8')

x_values = range(1,1001)

y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values,y_values, s=10)

# Define um titulo para o grafico
ax.set_title('Square Numbers', fontsize = 24)
# Define o titulo dos parametro de x
ax.set_xlabel('Values', fontsize = 14)
# Define o titulo dos parametro de y 
ax.set_ylabel('Squares', fontsize = 14)

# No tick params voce pode definir o tamanho dos rotulos do grafico
ax.tick_params(labelsize=14)

'''
axis define o intervalo que cada eixo tera no grafico 
comecando com o valor minimo (0) e maximo (1100) de x e terminando com os valores minimo (0) e maximo (1.100,000) de y 

o _ pode substituir a virgula e o ponto 

'''

ax.axis(0,1100,0,1_100_000)


# exibe os graficos do codigo 
plt.show()
