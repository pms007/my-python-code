#AssertionErrors provide a way to alert the programmer to mistakes during development

#assert keyword to report development errors

chars = ['Alpha','Beta','Gamma','Delta','Epslion']

def display (elem) :

	assert type(elem) is int, 'Argument must be integer'

	print ('List element',elem,'=',chars[4])


display(4)

display(4/2)