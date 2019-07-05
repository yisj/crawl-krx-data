import csv
import os
from collections import namedtuple
from datetime import datetime

Stock = namedtuple('Stock', ['name', 'code'])


dates = list()

for root, dirs, files in os.walk('stock-list'):
    for f in files:
        filename, ext = os.path.splitext(f)
        if ext == '.csv':
            dates.append(datetime.fromisoformat(filename))


dates.sort()
latest_date = dates[-1]


stocks = list()
with open('stock-list/%s.csv' % latest_date.isoformat()) as f:
	r = csv.reader(f)
	for row in r:
		name = row[0].strip()
		code = row[1].strip()
		stocks.append(Stock(name, code))