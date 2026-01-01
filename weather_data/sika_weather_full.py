
from matplotlib import pyplot as plt
import csv
from pathlib import Path
from datetime import datetime

path = Path("weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)


dates = []
indice_de_chuva = []
temp_max = []
temp_min = []


for row in reader:
  try:
    date =datetime.strptime(row[2], "%Y-%m-%d") 
    t_max = int(row[7])
    t_min = int(row[8])
    prcp = float(row[5])

  except ValueError:
    print(f"Missing data for {date}")

  else:
    dates.append(date)
    temp_max.append(t_max)
    temp_min.append(t_min)
    indice_de_chuva.append(prcp)


fig, ax = plt.subplots()

ax.plot(dates, temp_max, c="red", alpha=0.5)
ax.plot(dates, temp_min, c="blue", alpha=0.5)
ax.fill_between(dates, temp_max, temp_min, facecolor="blue", alpha=0.1)

ax.set_xlabel("Datas", fontsize = 14)
ax.set_ylabel("Temperatura (F)", fontsize = 14)
ax.tick_params(axis="both", which="major", labelsize=10)



plt.show()


fig, ax = plt.subplots()
ax.plot(dates, indice_de_chuva, c="red", alpha=0.5)
ax.set_xlabel("Datas", fontsize = 14)
ax.set_ylabel("Precipitação (in)", fontsize = 14)
ax.tick_params(axis="both", which="major", labelsize=10)
plt.show()
