# Create a list of numbers. Create a program that will iterate through the list and save the highest (maximum) value. Print out this value. Assume all numbers in the list are greater than 0.

numbers = [1, 3, 4, 5, 6, 7, 10, 20, 3423, 40, 43, 80, 45]
maximum = 0
for i in numbers:
    if i > maximum:
        maximum = i
print(maximum)