# bottles:
print('Bottle Refund Calculator')
print('------------------------')
print()
small = int(input('Number of small bottles: '))
large = int(input('Number of large bottles: '))
refund_small = small * 0.10
refund_large = large * 0.25
refund_total = refund_small + refund_large
print()
print(f'The total refund is $'f'{refund_total:.2f}')