from die import Die
import plotly.express as px

die = Die()

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# print(results)

# verificando a frequencia com que cada numero aparece

frequency = []

poss_results = range(1, die.num_sides+1)
for sides in poss_results:
    result = results.count(sides)
    frequency.append(result)
    
print(frequency)
    
    
fig = px.bar(x=poss_results, y= frequency)
fig.show()