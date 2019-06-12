"""
Given some string variable, create a new string that is made up of every other
character in the original string. Use a loop to do this.
"""
string = input('Please enter a string: ')
new_string = ''
for i in range(len(string)):
    if i % 2 == 0:
        new_string += string[i]
print(new_string)