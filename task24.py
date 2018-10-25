i=0
i2=0
n=0
x=0
y=0
dimension=''
list1x=[]
list2x=["|",]
list3x=[]
list2y=["|",]
list3y=[]
value=0

def inputdimension(text,dimension,value):
 while True:
  try:
   value=int(raw_input(text+ " for dimension "+dimension))
   return value
   break
  except ValueError:
   print "Oops!  That was no valid number.  Try again..."

def printdimensionx(x):
 global i
 if int(x)>0:
  while i <= int(x)-1:
    list1x.append(" ---")
    list2x.append("   |")
    list3x.append(" ---")
    #print 1st row if x not 0 after lists populated x (i) times 
    i+=1
  print (''.join(list1x))
  print (''.join(list2x))
  print (''.join(list3x)) 
def printdimensiony(y):
 if int(y)>0:
     global i2
     global n

     #print next lines (y-1) till y-1 element (because elements starting from 0) times. therefore -2 in next cycle
     while i2 <= int(y)-2: # -2 because elements starting from 0 and x=1 means y=1 as well so 0,1 array elements should be removed
       #print list items x times on y axis
       while n<= int(x)-1: 
        list2y.append("   |")
        list3y.append(" ---")
        n+=1
       i2+=1
       print (''.join(list2y))
       print (''.join(list3y))

x=inputdimension("Enter amount of cells ","X",value)
y=inputdimension("Enter amount of cells ","Y",value)
printdimensionx(x)
printdimensiony(y)
