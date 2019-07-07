#Exception Handling

#Statements in the try block are all executed unless or until an exception occurs.

#finally statement can be used to specify statements to be executed after exceptions have been handled
day = 32

try :

	if day > 31 :

		raise ValueError('Invalid day number')

except ValueError as msg :

	print ('Progran found an',msg)


finally :

	print ('But Today is Beautiful')

