
import unicodedata

s = 'Röd'

print('Red String',s)

print('Type',type(s),'Length',len(s))

s = s.encode('utf-8')

print('Encoded string',s)

print('Type',type(s),'Length',len(s))

s = s.decode('utf-8')

print('Decoded string',s)

print('Type',type(s),'Length',len(s))

for i in range(len(s)) :

	print(s[i],unicodedata.name(s[i]),sep=':')


s = b'Gr\xc3\xb6n'

print('Green string',s.decode('utf-8'))

s = 'Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}n'

print('Green String',s)



