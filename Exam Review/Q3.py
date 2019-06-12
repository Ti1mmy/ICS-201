"""
Create a program that will give the user the option to choose from a small(8.99)
, medium(10.99) and large(12.99) pizza as well as the quantity.
Calculate and display the subtotal, the tax and the grand total.

"""

option = input("Which pizza would you like? (Please enter 'small', "
               "'medium', or 'large'. ")
amount = int(input('How many would you like? '))

if option == 'small':
    price = 8.99
elif option == 'medium':
    price = 10.99
elif option == 'large':
    price = 12.99
else:
    print('Please enter a valid value')
subtotal = price * amount
total = subtotal * 1.13

if option == 'small' or 'medium' or 'large':
    print('Reciept')
    print('------------------------------------------------------------------')
    print()
    print(f'Subtotal: ${subtotal:.2f}')
    print(f'Tax: ${(total - subtotal):.2f}')
    print(f'Total: ${total:.2f}')
    print()
    print(f'Thanks for shopping!')