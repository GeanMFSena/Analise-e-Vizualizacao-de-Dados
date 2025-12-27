from pathlib import Path
import csv
from matplotlib import pyplot as plt
from datetime import datetime


path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

dates = []
heighs = []
for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(current_date)
    tmax = int(row[4])
    heighs.append(tmax)
    
# print(heighs)

# first_date = datetime.strptime('2021-07-01','%Y-%m-%d')
# print(first_date)


plt.style.use('seaborn-v0_8')

fig,ax = plt.subplots()

ax.plot(dates,heighs, color = 'red')

ax.set_title('Daily High Temperatures, July 2021', fontsize=24)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=14)
ax.tick_params(labelsize = 16)

plt.show()