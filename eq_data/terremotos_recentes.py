from pathlib import Path 
import json 
import plotly.express as px

path = Path('eq_data/all_day_arrumado.geojson')
content = path.read_text()
all_eq_data = json.loads(content)

all_eq_dicts = all_eq_data['features']

mags, longitude, latitude,title = [],[],[],[]

for dicts in all_eq_dicts:
    mag = dicts['properties']['mag']
    if mag < 0 or mag is None:
        mag = 0
    longs = dicts['geometry']['coordinates'][0]
    lats = dicts['geometry']['coordinates'][1]
    tit = dicts['properties']['title']
    mags.append(mag)
    longitude.append(longs)
    latitude.append(lats)
    title.append(tit)
    

eq_title = all_eq_data['metadata']['title']

fig = px.scatter_geo(lat=latitude, lon=longitude, title=eq_title,color=mags,size = mags,color_continuous_scale='magma',labels={'color':'Magnitude'},projection= 'natural earth',hover_name=title)

fig.show()