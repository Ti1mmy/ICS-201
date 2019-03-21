print('Feet -> Acre Generator')
print('========================')
print()
length = int(input('What is the length of the field in feet?: '))
width = int(input('What is the width of the field in feet?: '))
sq_feet = length * width
acres = sq_feet / 43560
print(f'The field is {round(acres, 2)} acres')