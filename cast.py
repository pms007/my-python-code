#Type Casting

a = input('Enter number: ')

b = input('\nEnter another number: ')

c = a + b

print ('\nData type of c is',type(c),c)

d = int(a) + int(b)

print ('\nData type of d is',type(d),d)

e = float(d)

print ('\nData type of e is',type(e),e)

f = chr(int(d))

print ('\nData type of f is',type(f),f)