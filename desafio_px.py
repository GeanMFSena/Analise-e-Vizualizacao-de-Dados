import plotly.express as px
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

fig = px.scatter(x=rw.x_values, y=rw.y_values, labels={'x':'Values','y':'Squares'}, title='Squares')

fig.show()