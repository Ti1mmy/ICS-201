print('Shape Namer: ')
print()
n = int(input('Please type the number of sides of your shape(n): '))
if n < 3:
    print('A polygon must have at least three sides.')
elif n == 3:
    print('The shape is a triangle.')
elif n == 4:
    print('The shape is a square.')
elif n == 5:
    print('The shape is a pentagon')
elif n == 6:
    print('The shape is a hexagon.')
elif n == 7:
    print('The shape is a heptagon.')
elif n == 8:
    print('The shape is an octagon.')
elif n == 9:
    print('The shape is a nonagon.')
elif n == 10:
    print('The shape is a decagon.')
elif n == 11:
    print('The shape is a dodecagon.')
elif n > 11:
    print('This program only supports shapes up to 11 sides. If you would like to know the names, visit:')
    print(f'https://www.google.com/search?q=what+shape+has+{n}+sides')