# • Variable – stores a single value
# • List – stores multiple values in an ordered index
# • Tuple – stores multiple fixed values in a sequence
# • Set – stores multiple unique values in an unordered collection
# • Dictionary – stores multiple unordered key:value pairs

dict = {'name':'Bob','ref':'Python','sys':'Linux'}

print ('Dictionary',dict)

print ('Reference',dict['ref'])

print ('Keys',dict.keys())

del dict['name']

dict['user'] = 'Tom'

print ('Dictionary',dict)

print ('Is there a name key','name' in dict)