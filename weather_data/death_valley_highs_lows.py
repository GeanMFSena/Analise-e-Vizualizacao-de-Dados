from pathlib import Path
from matplotlib import pyplot as plt
from datetime import datetime
import csv

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

dates,highs,lows = [],[],[]

# print(header_now)

for index, colum_header in enumerate(header_row):
    print(index, colum_header)
    
for row in reader:
    try:
        high = int(row[3])
        low = int(row[4])
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
    
fig,ax = plt.subplots()

ax.plot(dates, highs, color = 'red', alpha = 0.6)
ax.plot(dates, lows, color = 'blue', alpha = 0.6)

ax.fill_between(dates, highs, lows, alpha = 0.3)
ax.set_title(f'Daily High and Low temperature, 2021\nDeaths Valley, CA', fontsize=20)
ax.set_xlabel('', fontsize = 16)

plt.show()
