import math
print('Human Years to Dog Years Calculator:')
print()
human_years = float(input('How old is the dog in human years? '))
if human_years <= 2 and human_years > 0:
    print(f'The dog is {round(human_years * 10.5)} years old in dog years.')
elif human_years > 2:
    print(f'The dog is {round(((human_years - 2) * 4 + 21), 2)} years old in dog years.')
else:
    print(f'Error: The number {human_years} is negative!')
