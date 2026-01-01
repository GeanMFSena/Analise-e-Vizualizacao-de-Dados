import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

fig, ax = plt.subplots()

ax.plot(rw.x_values, rw.y_values, c='green',linewidth = 5,)

ax.set_title('Squares', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Squares', fontsize=14)

ax.set_aspect('equal')

plt.show()