# How do you swap two numbers without using the third variable?
# Example, x=4, y=9  ==>  x=9, y=4

x, y = 4, 9

print('before swap, x=', x, ' y=', y)
x = x + y
y = x - y
x = x - y
print('after swap, x=', x, ' y=', y)