#Set

# Set Method: Description:
# set.add(x) Adds item x to the set
# set.update(x,y,z) Adds multiple items to the set
# set.copy() Returns a copy of the set
# set.pop() Removes one random item from the set
# set.discard( i ) Removes item at position i from the set
# set1.intersection(set2) Returns items that appear in both sets
# set1.difference(set2) Returns items in set1 but not in set2

zoo = ('Kangaroo','Leopard','Moose')

print ('Tuple',zoo,'Length',len(zoo))

print ('Type',type(zoo))

bag = {'Red','Green','Blue'}

bag.add('Yellow')

print ('\nSet',bag,'Length',len(bag))

print ('Type',type(bag))

print ('Is green in bag','Green' in bag)

print ('Is orange in bad','Orange' in bag)

box = {'Red','Purple','Yellow'}

print ('Box',box,'Length',len(box))

print ('Common to both set',bag.intersection(box))

print ('Diff to both set',bag.difference(box))