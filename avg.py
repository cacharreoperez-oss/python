import sys


total = 0
count = 0

for value in sys.argv[1:]:
	total += float(value)
	count += 1

average = total / count
print(f'{average:.2f}')