#yield - specifies the generator object to be returned to the caller

#next specify that variable name within its parentheses to continue execution of the function

def fibonanci_generator() : 

	a = b = 1

	while True:
		
		yield a

		a,b = b , a + b

fib = fibonanci_generator()		


for f in fib :

	if f > 100 :

		break

	else :
	
		print ('Generated',f)	




