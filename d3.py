from die import Die
import plotly.express as px 

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []

for roll in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
# print(results)

max_roll = die_1.num_sides + die_2.num_sides + die_3.num_sides

poss_results = range(3, max_roll+1)

frequencies = []

for sides in poss_results:
    frequency = results.count(sides)
    frequencies.append(frequency)
    
print(frequencies)

fig = px.bar(x=poss_results,y=frequencies, title='Results of rolling tree d6 1,000 times',labels={'x':'Sides','y':'Frequency'})

fig.update_layout(xaxis_dtick=1)

fig.show()