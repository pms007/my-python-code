#Function with return

num = input('Enter a number ')


def square (num) :

	if not num.isdigit() :

		return 'Invalid Input'

	num = int (num)
		
	return num * num

print (num,'square is =',square(num))			