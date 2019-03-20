year = int(input('Type in the year: '))
century_base = year // 100
if year % 100 > 0:
    print(century_base + 1)
else:
    print(century_base)