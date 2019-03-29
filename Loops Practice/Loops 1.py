print('    Cost             With tax')
print('-------------------------------')
for price in range(10, 51, 5):
    tax = price * 1.15
    print(f'    ${price:.2f}           ${tax:.2f}')