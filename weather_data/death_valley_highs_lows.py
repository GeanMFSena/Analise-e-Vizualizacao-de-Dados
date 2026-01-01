from pathlib import Path
from matplotlib import pyplot as plt
from datetime import datetime
import csv

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

sika_path = Path('weather_data/sitka_weather_2021_simple.csv')
sika_lines = sika_path.read_text().splitlines()

sika_reader = csv.reader(sika_lines)
sika_header_now = next(sika_reader)

sika_dates,sika_highs,sika_lows = [],[],[]
dates,highs,lows = [],[],[]

# print(header_now)

for index, colum_header in enumerate(header_row):
    print(index, colum_header)
    
    
for sika_row in sika_reader:
    try:
        sika_high = int(sika_row[4])
        sika_low = int(sika_row[5])
        sika_current_date = datetime.strptime(sika_row[2],'%Y-%m-%d')
    except ValueError:
        print(f'Missing data for {sika_current_date}')
    else:
        sika_highs.append(sika_high)
        sika_lows.append(sika_low)
        sika_dates.append(sika_current_date)    

    
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
ax.plot(dates, sika_highs, color = 'green', alpha = 0.6)
ax.plot(dates, sika_lows, color = 'purple', alpha = 0.6)


ax.fill_between(dates, highs, lows, alpha = 0.3)
ax.set_title(f'Daily High and Low temperature, 2021\nDeaths Valley, CA', fontsize=20)
ax.set_xlabel('', fontsize = 16)

plt.show()
