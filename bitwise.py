#Bitwise

a = 10

b = 5

print ('a=',a,'b=',b)

# 1010 ^ 0101 = 1111 (decimal 15)
a = a ^ b

print ('a=',a)

# 1111 ^ 0101 = 1010 (decimal 10)

b = a ^ b

print ('b=',b)