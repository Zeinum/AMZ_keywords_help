import csv
import dataset
db = dataset.connect('sqlite:///:memory:')
table = db['ppc']

f = "Sample_data/search-term-report-2017-08-25-118862017464.txt"


with open(f, 'r') as report:
    reader = csv.DictReader(report, delimiter='\t')
    for row in reader:
        table.insert(row)

print(db.tables)
print(db['ppc'].columns)

for item in db['ppc'].distinct('Customer Search Term'):
    print(item)