#import random
from random import randrange
n=0
list1=[]
list2=[]
list3=[]


def generatelist(listname):
 n=0
 while n<=2:
  listname.append(randrange(0,3))
  n+=1
 print listname

def main():
 list1=[]
 list2=[]
 list3=[]
 generatelist(list1)
 generatelist(list2)
 generatelist(list3)
 checkwinner(list1,list2,list3)

def checkwinner(list1,list2,list3): 
 print ""
 n=0 
 while n <=2:
#  print "list1 item "+str(n) + " = "+str(list1[n])
#  print "list2 item "+str(n) + " = "+str(list2[n])
#  print "list3 item "+str(n) + " = "+str(list3[n])
  if list1[n]==list2[n] and list2[n]==list3[n]:
   print "player won by horizontal" 
   raise SystemExit
  n+=1  
 if list1[0]==list2[1] and list2[1]==list3[2]:
  print "player won by diagonal from left to right"
  raise SystemExit
 if list3[0]==list2[1] and list2[1]==list1[2]:
  print "player won by diagonal from right to left"
  raise SystemExit
 else:
  main() 

main()
