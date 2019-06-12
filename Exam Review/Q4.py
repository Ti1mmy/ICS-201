"""
Create a loop to add the numbers from variable a to variable b.
You can fill in their literal values.
"""

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
sum = []
for i in range(len(a)):
    sum.append(a[i] + b[i])
print(sum)