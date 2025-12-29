from matplotlib import pyplot as plt
from pathlib import Path    
import csv
from datetime import datetime

dates,heighs,lows = [],[],[]

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_now = next(reader)
# print(header_now)

for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    heigh = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    heighs.append(heigh)
    lows.append(low)
    
# plota as temperaturar maximas e minimas

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()

ax.plot(dates,heighs,color = 'red')
ax.plot(dates,lows, color = 'blue')

ax.set_title('Daily High and Low temperatures, 2021', fontsize=24)
ax.set_xlabel('Dates',fontsize = 14)
ax.set_ylabel('Temperatures', fontsize = 14)

plt.show()