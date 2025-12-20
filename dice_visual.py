from die import Die
import plotly.express as px

die_1 = Die(8)
die_2 = Die(8)

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# print(results)

# analisa a frequencia

frequencies = []

max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)

for sides in poss_results:
    frequency = results.count(sides)
    frequencies.append(frequency)
    
fig = px.bar(x=poss_results, y=frequencies, labels={'x':'Result','y':'Frequency'}, title='Results of rolling one d8 and d8 1,000 times')

fig.update_layout(xaxis_dtick=1)
    
fig.write_html('d8x2.html')
fig.show()
    
    