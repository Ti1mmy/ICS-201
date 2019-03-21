print('Chinese Zodiac Calculator')
print()
year = int(input('Please type in the year: '))
if year < 0:
    print('Error: Year cannot be negative.')
elif (year - 8) % 12 == 0:
    print(f'{year} is the year of the dragon.')
elif (year - 8) % 12 == 1:
    print(f'{year} is the year of the snake.')
elif (year - 8) % 12 == 2:
    print(f'{year} is the year of the horse.')
elif (year - 8) % 12 == 3:
    print(f'{year} is the year of the sheep.')
elif (year - 8) % 12 == 4:
    print(f'{year} is the year of the monkey.')
elif (year - 8) % 12 == 5:
    print(f'{year} is the year of the rooster.')
elif (year - 8) % 12 == 6:
    print(f'{year} is the year of the dog.')
elif (year - 8) % 12 == 7:
    print(f'{year} is the year of the pig.')
elif (year - 8) % 12 == 8:
    print(f'{year} is the year of the rat.')
elif (year - 8) % 12 == 9:
    print(f'{year} is the year of the ox.')
elif (year - 8) % 12 == 10:
    print(f'{year} is the year of the tiger.')
elif (year - 8) % 12 == 11:
    print(f'{year} is the year of the hare.')
