from re import *

pattern = compile('(^)[-a-z0-9_.]+@([-a-z0-9]+.)+[a-z]{2,6}($)')

def get_address() :

	address = input('Enter your email address ')

	is_valid = pattern.match(address)

	if is_valid :

		print ('Email valid',is_valid.group())

	else :
	
		print ('Invalid Address Please retry\n')	


get_address()
