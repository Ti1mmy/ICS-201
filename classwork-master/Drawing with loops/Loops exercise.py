"""
# 1.
sum = 0
for i in range(10):
    i = int(input('Please enter a number: '))
    sum += i
print(sum)
"""
#2
vowels = 'aeiouAEIOU'
total = 0
for i in range(10):
    i = input('Please type in a letter: ')
    if i == '':
        num = 0
    elif i in vowels:
        num = 1
    else:
        num = 0
    total += num
print(total)