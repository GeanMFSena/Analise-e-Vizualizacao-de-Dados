from pathlib import Path
import json

# le os dados como uma string e converte em um objeto python 

path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# criando um novo arquivo com os dados formatados
# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent= 4)
# path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))


mags,longitudes, latitudes = [],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lons = eq_dict['geometry']['coordinates'][0]
    lats = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    longitudes.append(lons)
    latitudes.append(lats)
    
print(mags[:10])
print(longitudes[:5])
print(latitudes[:5])

    