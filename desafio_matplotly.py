import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll()+die_2.roll()+ die_3.roll() for roll in range(1000)]


max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_result = range(3,max_result+1)

frequencies = [results.count(sides) for sides in poss_result]
print(frequencies)

fig,ax = plt.subplots()

plt.style.use('seaborn-v0_8')

ax.bar(poss_result,frequencies, color='green')
ax.set_title('Rolagem de dados de 3 lados 1000 vezes', fontsize=24)
ax.set_xlabel('Numero dos lados', fontsize=14)
ax.set_ylabel('Frequencia dos lados', fontsize=14)

plt.show()