#random.sample() does not actually replace elements of the sequence but merely copies a sample,

import math,random

print ('Round up 9.5 =',math.ceil(9.5))

print ('Round down 9.5 =',math.floor(9.5))

num = 4

print(num,'Square is',math.pow(num,2))

print(num,'Square root',math.sqrt(num))

nums = random.sample(range(1,49),6)

print('Your lucky numbers are',nums)