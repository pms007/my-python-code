from datetime import *

today = datetime.today()

print('Today is',today)

for attr in ['year','month','day','hour','minute','second','microsecond'] :

	print(attr,'\t',getattr(today,attr))



print ('Time',today.hour,'Minute',today.minute)

day = today.strftime('%A')

month = today.strftime('%B')

print ('Date',day,month,today.day)	