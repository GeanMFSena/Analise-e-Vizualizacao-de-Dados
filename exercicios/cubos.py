import matplotlib.pyplot as plt

# plt.style.use('seaborn-v0_8')

# x_values = [1,2,3,4,5]

# y_values = [ x**3 for x in x_values ]

# fig,ax = plt.subplots()

# ax.scatter(x_values, y_values, c= y_values, cmap = plt.cm.Blues, s=10)

# plt.show()

plt.style.use('seaborn-v0_8')

x_values = range(1,5001)

y_values = [x**3 for x in x_values ]

fig,ax = plt.subplots()

ax.scatter(x_values, y_values, c= y_values, cmap = plt.cm.Blues, s=10)

ax.set_title('Squares', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Squares', fontsize=14)

ax.tick_params(labelsize = 10)
ax.ticklabel_format(style= 'plain')

plt.show()
