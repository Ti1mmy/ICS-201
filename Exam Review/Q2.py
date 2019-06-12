"""
Ask the user to input a number from 1-5 rating a restaurant's service.
Depending on what they rate the restaurant, the program will output an appropriate message from
1 ->“We are very sorry” to
5 -> “Great! We are glad you enjoyed yourself!”.

"""

response = [
    'We are very sorry',
    'Please give us another try',
    'We hope to see you again!',
    "Let's hope the next is even better!",
    'Great! We are glad you enjoyed yourself!'
]
rating = int(input('Please rate our service from a level of 1 through 5. '))

if 0 < rating < 6:
    print(response[rating - 1])
else:
    print('Please enter a number from one through five.')
