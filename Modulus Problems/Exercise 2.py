total_minutes = int(input('Enter the number of minutes: '))
hours = total_minutes // 60
minutes = total_minutes % 60
print(f'{hours:02}:'f'{minutes:02}')