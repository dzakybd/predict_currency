import requests
import csv
import json
from datetime import datetime, timedelta

now = datetime.now()
lastyear = now - timedelta(days=365)
curr_1 = 'KRW'
curr_2 = 'IDR'
end_date = now.strftime("%Y-%m-%d")
start_date = lastyear.strftime("%Y-%m-%d")
url = "https://api.exchangeratesapi.io/history?start_at={}&end_at={}&base={}&symbols={}".format(start_date, end_date, curr_1, curr_2)
response = requests.get(url).json()
result = json.loads(json.dumps(response))

print(url)
print(response)

csv_data = []
for i in result["rates"]:
    rate = result["rates"][i]["IDR"]
    print(i, rate)
    csv_data.append([i, rate])

with open('dataset.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csv_data)

csvFile.close()