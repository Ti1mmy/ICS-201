number = int(input('Enter your number: '))
if number % 3 == 0 and number % 4 == 0:
    print(f'{number} is a multiple of 3 and 4')
elif number % 3 == 0:
    print(f'{number} is a multiple of 3')
elif number % 4 == 0:
    print(f'{number} is a multiple of 4')
else:
    print(f'{number} is neither a multiple of 3 nor 4')