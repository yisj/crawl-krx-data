import csv
import os
from datetime import datetime


if not os.path.exists('stock-list'):
    os.mkdir('stock-list')


dates = list()

for root, dirs, files in os.walk('krx-stock'):
    for f in files:
        filename, ext = os.path.splitext(f)
        if ext == '.csv':
            dates.append(datetime.fromisoformat(filename))



dates.sort()
latest_date = dates[-1]



stock_list = list()
with open('krx-stock/%s.csv' % latest_date.isoformat()) as f:
    stockreader = csv.reader(f)
    for i, row in enumerate(stockreader):
        if i > 0:
            stock_list.append('%s, %06d' % (row[1], int(row[2])))


with open('stock-list/%s.csv' % latest_date.isoformat(), 'w') as f:
    f.write('\n'.join(stock_list))
