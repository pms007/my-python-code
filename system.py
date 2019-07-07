
import sys,keyword


print ('Python version',sys.version)

print ('Python Interpreter location',sys.executable)

for dir in sys.path :

	print (dir)



for word in keyword.kwlist :

	print (word)
