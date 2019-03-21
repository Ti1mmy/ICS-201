# Create a program that will ask the user for a word. The program will iterate through the string and print out each character except for the vowels.
word = input('Please type in a word: ')
# vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'] # doesn't work for replace(), therefore used string
include_y = input('Consider y a vowel? (y/n): ')
if include_y != 'y':
    vowels = 'aeiouAEIOU'
else:
    vowels = 'aeiouyAEIOUY'
for char in vowels:
    word = word.replace(char, "")
for character in word:
    print(character)
