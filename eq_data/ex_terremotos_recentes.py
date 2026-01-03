from pathlib import Path
import plotly.express as px 
import json 


path = Path('eq_data/all_day.geojson')
content = path.read_text()
all_eq_data = json.loads(content)

path = Path('eq_data/all_day_arrumado.geojson')
data_arrumado = json.dumps(all_eq_data, indent= 4)
path.write_text(data_arrumado)
