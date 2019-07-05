from stocks import stocks
import sys

code = sys.argv[1]

for stock in stocks:
	if stock.code == code:
		target_code = stock.code
		target_name = stock.name


print(target_code, target_name)