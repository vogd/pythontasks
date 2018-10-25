import random
sortedl=[]
mylist=[]
iteration=0
i=17
n=0 
trueval=0

def generatelist(iteration,i):
 iteration=iteration+1
 print ("Iteration " + str(iteration))
 mylist=random.sample(range(50),10)
 mylist == mylist.sort()
 print (mylist)
 checklistbinary(mylist,iteration,i)
#checklist(mylist,iteration)

#def checklist(mylist,iteration):
# if (i in mylist):
#  print ("Hurray " + str(i) + " is a part of the list ! " + str(mylist))
#  raise SystemExit
# else:
#  generatelist(iteration)   

def checklistbinary(mylist,iteration,i):
  compare=len(mylist)
  compare = int(compare/2)
  for n in xrange(0,len(mylist)-1):
   print ("Starting division from list itemID "+str(compare))
   if int(mylist[compare])>i:
    print ("ItemID "+str(compare)+ " is: "+str(mylist[compare])+" > " + str(i))
    compare = compare-n
    #print(compare)
    trueval=1
   elif int(mylist[compare])==i:
       print ("ItemID " +str(compare)+" is: " + str(mylist[compare])+ " =  " + str(i)) 
       print ("Item found in the list. Exiting..")
       raise SystemExit
   elif int(mylist[compare])<i:
    #print(compare)   
    print ("Item "+str(compare)+ "is: " +str(mylist[compare])+" < " + str(i))
    compare = compare+n
    print ("Next List item index is " +str(compare))
    compare = int(compare/2)
    trueval=0
  if trueval==1:
   print ("Value is withing the list range, but there is no direct match") 
   print ("Startig new interaction unless the list will have direct match")
   generatelist(iteration,i)
  else:
   print ("Value is not withing the list. Starting new iteration unless item will be found..")
   generatelist(iteration,i)
generatelist(iteration,i)
