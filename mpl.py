import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25] 

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values,squares, linewidth=3)
# ax.plot(input_values,squares,linewidth=3)


# define o titulo do grafico e os eixos do rotulo 

ax.set_title('Square Numbers',fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)           
ax.set_ylabel('Square of value', fontsize = 14)

# define o tamanho dos rotulos de marcacao de escala 
ax.tick_params(labelsize = 14)

plt.show()


plt.style.use('seaborn-v0_8')

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25] 

fig2,ax2, = plt.subplots()

ax2.scatter(x_values,y_values, s=200)

ax2.set_title('Square Numbers', fontsize = 24)
ax2.set_xlabel('Value', fontsize= 14)
ax2.set_ylabel('Square', fontsize=14)

ax2.tick_params(labelsize=14)

plt.show()

