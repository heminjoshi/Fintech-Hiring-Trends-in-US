import json
import csv
with open('results.json', 'r') as f:
	data = json.load(f)
		
with open("data.csv", "w") as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['jobID'], item['link']] + item['jobT'] + item['jobD'].values())