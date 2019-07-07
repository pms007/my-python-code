
file = open('example.txt','w')


print ('File Name',file.name)

print ('File Open Mode',file.mode)

print ('Readable',file.readable())

print ('Writable',file.writable())

def get_status(f) :

	if (f.closed != False) :

		return 'closed'

	else :
	
		return 'open'

print ('file status',get_status(file))		

file.close()

print ('file status',get_status(file))	
