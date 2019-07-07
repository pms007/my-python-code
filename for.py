#Looping over items

chars = ['A','B','C']

fruit = ('Apple','Banana','Cherry')

dict = {'name':'Bob','ref':'Python','sys':'Linux'}

print ('Elements')

for item in chars :
	
	print (item)

#display all list element values and their relative index number

print ('Enumerated')

for item in enumerate(chars) :

	print (item)

#display all list and tuple elements

for  item in zip(chars,fruit) :
	
	print (item)


#display all dictionary key names and associated element values

for key,value in dict.items() :

	print (key,'=',value)