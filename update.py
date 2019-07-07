
text = 'The political slogan “Workers Of The World Unite!” is from The Communist Manifesto.'

with open('update.txt','w') as file :

	file.write(text)

	print('Now file closed',file.closed)


with open('update.txt','r+') as file :

	text = file.read()

	print('String',text)

	print('Position file now',file.tell())

	position = file.seek(32)

	print('Position file now',file.tell())

	file.write('All Lands')

	file.seek(58)

	file.write('the tombstone of Karl Marx.')

	file.seek(0)

	text = file.read()

	print('String',text)
