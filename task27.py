from random import randrange

i=0
n=0
symbol=0
coord=''
coordlist=[]
list1=[]
list2=[]
list3=[]
available1=[]
available2=[]
available3=[]
winner=0

def generatelist(listname):
 n=0
 while n<=2:
  listname.append("")
  n+=1
 print listname

player1=1
player2=0


def readmove(player):
 coord=raw_input("Input player "+str(player)+" move coordinates x,y : ")
 coordlist=list(coord)  
 x=(int(coordlist[0])-1)
 y=int(coordlist[2])
 if int(x)<0 or int(y)==0:
  print "Please enter new coordinates for the move. Axis value can not be '0'"
  readmove(player)
 else: 
  if int(player)==1:
   symbol==0
   print "Will call func to update list with '0'"
   placemove(symbol,x,y,player)
  else:
   symbol==1
   print "Will call func to update list with '1'"
   placemove(symbol,x,y,player)

def placemove(symbol,x,y,player):
 if int(y)==1:
  if list1[int(x)]<>0 and list1[int(x)]<>1:
   print "appending list1"
   list1[int(x)]=int(symbol)
  else:
   print "please enter new coordinates, that slot is already used"
   readmove(player)
 elif int(y)==2:
  if list2[int(x)]<>0 and list2[int(x)]<>1:
   print "appending list2"
   list2[int(x)]=int(symbol)
  else:
   print "please enter new coordinates, that slot is already used"
   readmove(player)
 elif int(y)==3:
  if list3[int(x)]<>0 and list3[int(x)]<>1:
   print "appending list3"
   list3[int(x)]=int(symbol)
  else:
   print "please enter new coordinates, that slot is already used"
   readmove(player)

 else:
   print "Enter Valid X cordinates from 1 to 3 one more time !!! : "
   readmove(player)
 print list1
 print list2
 print list3

generatelist(list1)
generatelist(list2)
generatelist(list3)

while int(winner)<>1:
  readmove(1)
  readmove(2)

#checklist (list1,available1)
