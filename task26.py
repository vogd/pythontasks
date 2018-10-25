#import random
from random import randrange
n=0
list1=[]
list2=[]
list3=[]


def generatelist(listname):
 #global n
 n=0
 while n<=2:
  listname.append(randrange(0,3))
  n+=1
 print listname

generatelist(list1)
generatelist(list2)
generatelist(list3)

while n <=2:
  print "list1 item "+str(n) + " = "+str(list1[n])
  print "list2 item "+str(n) + " = "+str(list2[n])
  print "list3 item "+str(n) + " = "+str(list3[n])
  n+=1 
