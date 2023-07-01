import math
x = float(input())
y = float(input())
z = float(input())
first = x ** z
second = x ** (y ** z)
third = abs(x - y)
fourth = math.sqrt((x ** z))
print(f'{first:.2f} {second:.2f} {third:.2f} {fourth:.2f}')