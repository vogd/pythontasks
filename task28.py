def inputvalues():
  x=int(raw_input("Enter variable1: "))
  y=int(raw_input("Enter variable2: "))
  z=int(raw_input("Enter variable3: "))

  if x>=y :
   if x>=z:
     print "variable1 is max: " + str(x)+ " > " +str(y)+" > "+ str(z)
   else:
     print "variable3 is max: " + str(z)+ " > " +str(x)+" > "+ str(y)
  else: 
   if y>=z:
     print "variable2 is max: " + str(y)+ " > " +str(z)+" > "+ str(x)
   else:
     print "variable3 is max: " + str(z)+ " > " +str(x)+" > "+ str(y)

inputvalues()

