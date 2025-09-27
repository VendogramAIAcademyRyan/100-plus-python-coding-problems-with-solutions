a = 2
b = 3
print(a, b)

temp = a 
a = b
b = temp
print(a,b)

a, b = b, a
a, b = b, a
print(a, b)