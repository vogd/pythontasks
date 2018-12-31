def checkdigit(f):
 list1=range(2,f)
 print list1
 for i in list1:
  if f%i==0: 
   return f

d=int(raw_input("Enter digit :"))
result=checkdigit(d)
if result:
 print str(result)+"-Is a Prime !!! "
else:
 print str(d)+"-Not a prime"

