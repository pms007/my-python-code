#list fun

# List Method: Description:
# list.append(x) Adds item x to the end of the list
# list.extend(L) Adds all items in list L to the end of the list
# list.insert(i,x) Inserts item x at index position i
# list.remove(x) Removes first item x from the list
# list.pop(i) Removes item at index position i and returns it
# list.index(x) Returns the index position in the list of first item x
# list.count(x) Returns the number of times x appears in the list
# list.sort() Sort all list items, in place
# list.reverse() Reverse all list items, in place

basket = ['Apple','Bun','Cola']

crate = ['Egg','Fig','Grape']

print ('Basket list',basket)

print ('Basket elements',len(basket))

basket.append('Damson')

print ('Basket Append',basket)

print ('Last basket item removed',basket.pop())

print ('Basket list',basket)

basket.extend(crate)

print ('Extended basket list',basket)

del basket[1]

print ('Item remove',basket)

del basket[1:3]

print ('Slice removed',basket)