subtotal = 0
items = []
for i in range(1, 6):
    item_cost = int(input(f'Please type in the cost of item {i}: '))
    subtotal += item_cost
    items.insert(i, item_cost)
print('Final Receipt')
print()
print('    Cost             With tax')
print('-------------------------------')
for item in range(5):
    print(f'    ${(items[item]):.2f}           ${((items[item]) * 1.15):.2f}')
print()
print('    Subtotal        Total')
print('-------------------------------')
print(f'    ${subtotal}           ${subtotal * 1.15}')