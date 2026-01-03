import plotly.express as px 
from pathlib import Path
import json

path = Path('eq_data/readable_eq_data.geojson')
content = path.read_text()
all_eq_data = json.loads(content)

all_eq_dicts = all_eq_data['features']

mags, longitude, latitude, eq_title = [],[],[],[]

for dicts in all_eq_dicts:
    # mag = dicts['properties']['mag']
    # longs = int(dicts['geometry']['coordinates'][0])
    # lats = int(dicts['geometry']['coordinates'][1])
    # tit = dicts['properties']['title']
    mags.append(dicts['properties']['mag'])
    longitude.append(int(dicts['geometry']['coordinates'][0]))
    latitude.append(int(dicts['geometry']['coordinates'][1]))
    eq_title.append(dicts['properties']['title'])
    
title = all_eq_data['metadata']['title']

print(mags[:10])
print(longitude[:5])
print(latitude[:5])
    
fig = px.scatter_geo(lat= latitude, lon= longitude,size= mags, title = title, color= mags, color_continuous_scale='magma', labels={'color':'Magnitude'}, projection='natural earth',hover_name=eq_title)
fig.show()