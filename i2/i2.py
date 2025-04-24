import json
import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def read_json_file(filename):
    with open(filename) as file:
        data = json.load(file)
    return data

def read_csv_file(filename):
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
    return data

json_dict = read_json_file("/Users/selinaliu/Desktop/IMT542_individual/i2/PS4Games.json")
csv_dict = read_csv_file("/Users/selinaliu/Desktop/IMT542_individual/i2/vgchartz-2024.csv")


def create_combined_dataset(json_data, csv_data):
    new_dataset = []

    for game in json_data:
        game_name = game['Game'].strip().lower()
        for row in csv_data:
            csv_title = row['title'].strip().lower()
            if game_name == csv_title and row['na_sales']:
                new_entry = {
                    'Game': game['Game'],
                    'NA_Sales': float(row['na_sales']),
                    'Release_Year': game['Year']
                }
                new_dataset.append(new_entry)
                break  # Stop after first match
    return new_dataset

combined_dataset = create_combined_dataset(json_dict, csv_dict)
# print(combined_dataset)

sales_by_year = defaultdict(float)

# Filter out bad/missing years
for entry in combined_dataset:
    year = entry['Release_Year']
    sales = entry['NA_Sales']
    
    try:
        year = int(year)
        sales_by_year[year] += sales
    except (TypeError, ValueError):
        continue

sorted_years = sorted(sales_by_year.keys())
sorted_sales = [sales_by_year[year] for year in sorted_years]

plt.figure(figsize=(10, 6))
plt.plot(sorted_years, sorted_sales, marker='o', linestyle='-', color='skyblue')
plt.title('Total NA Sales by Release Year')
plt.xlabel('Release Year')
plt.ylabel('NA Sales (in millions)')
plt.grid(True)
plt.tight_layout()
plt.show()