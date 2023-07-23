import csv
from datetime import datetime

filename = 'data_weather_Moscow_Sheremetyevo_2022.csv'

with open(filename) as file:
    reader = csv.reader(file)
    headers = next(reader)
    data_list = [row for row in reader]

received_data = {}

current_data = [datetime.strptime(data[0], "%d.%m.%Y") for data in data_list]
received_data['date'] = current_data

for index, column_header in enumerate(headers):
    if index == 0:
        continue
    current_data = [float(data[index]) for data in data_list]
    received_data[column_header] = current_data
