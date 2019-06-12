"""
Given some string, create a new string that is a copy of the original string
but without vowels. Use a loop to do this.
"""

string = (input('Please type in a string: '))
vowels = ['a', 'e', 'i', 'o', 'u']
for vowel in vowels:
    string = string.replace(vowel, "")
    print(vowel)
print(string)