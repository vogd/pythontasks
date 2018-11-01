from random import randrange

i=0
n=0
list1=[]
list2=[]
list3=[]
available1=[]
available2=[]
available3=[]

def generatelist(listname):
 n=0
 while n<=2:
  listname.append(randrange(0,2))
  n+=1
 print listname



player1=1
player2=0

def checklist(customlist,customavailable):
  i=0
  while i<=2:
    if int(customlist[i])==0:
     print "item "+str(i)+ "used by player1"
    elif int(customlist[i])==1: 
     print "item "+str(i)+ "used by player2"
    else:
     print "Items available for a move :" + str(i)
     customavailable.append(i)
    i+=1

generatelist(list1)
checklist (list1,available1)
