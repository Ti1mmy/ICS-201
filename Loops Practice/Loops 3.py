# Calculating
subtotal = 0
items = []
item_cost = 0
item_number = 1
while item_cost != '':
        item_cost = input(f'Please type in the cost of item {item_number}: ')
        if item_cost == '':
            break
        else:
            subtotal += float(item_cost)
            items.insert(item_number, float(item_cost))
            item_number += 1
# Displaying
spaces_subtotal = ((11 - (len(str(int(subtotal))))) * ' ')
print()
print('Final Receipt:')
print()
print('    Cost             With tax')
print('-------------------------------')
for item in range(item_number - 1):
    spaces_items = ((11 - (len(str(int(items[item]))))) * ' ')
    print(f'    ${(items[item]):.2f}{spaces_items}${((items[item]) * 1.15):.2f}')
print('-------------------------------')
print('    Subtotal:        Total:')
print(f'${subtotal:.2f}{spaces_subtotal}${(subtotal * 1.15):.2f}')
