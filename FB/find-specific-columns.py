import csv
from collections import defaultdict

columns = defaultdict(list)

with open('dataset3.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

print(' '.join(columns['1']) +  '\n' + ' '.join(columns['3']))
