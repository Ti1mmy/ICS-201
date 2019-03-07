# Ask the user for their name. Create a program that will loop OVER A RANGE and print each character of their name on seperate lines. You will access each character by using the character's index value. E.g., char = name[0]

name = input('What is your name? ')
for i in range(len(name)):
    print(name[i])