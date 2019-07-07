#Function with arguments

def echo(user,lang,sys) : 

	print ('User :',user,'Language :',lang,'Platgform :',sys)



echo('Mike','Python','Linux')


def mirror(user = 'Bob',lang = 'Python') :

	print ('User',user,'Language',lang)


mirror()

mirror(lang = 'Java')

mirror(user = 'Pymyo')

mirror('PMS','PHP')
