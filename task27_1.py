from random import randrange

n=0
k=0
symbol=0
coord=''
coordlist=[]
list1=[]
list2=[]
list3=[]
winner=0

def generatelist(listname):
 n=0
 while n<=2:
  listname.append("")
  n+=1
 print listname

player1=1
player2=0

def checkmoves(list1,list2,list3):
  # Match lists and find if same position items in lists are the same (check by vertical)
  global k
  for k in list1:
   if k <> '':
    if k==0:
     winner=1 
    else: 
     winner=2
    if k in list2 and k in list3:
     print "Winner is player "+ str(winner)+ " !!!"
     raise SystemExit

# Check winner if All items in list1 are filled with values   
    if len(set(list1))==1: 
     print "Winner is player "+ str(winner)+ " !!!"
     raise SystemExit

# Check winner if All items in list2 are filled with values
  for k in list2:
   if k <> '':
    if k==0:
     winner=1 
    else: 
     winner=2
    if len(set(list2))==1: 
     print "Winner is player "+ str(winner)+ " !!!"
     raise SystemExit

# Check winner if All items in list3 are filled with values
  for k in list3: 
   if k <> '':
    if k==0:
     winner=1 
    else: 
     winner=2
    if len(set(list3))==1: 
     print "Winner is player "+ str(winner)+ " !!!"
     raise SystemExit

#Check winner by diagonal
  if list1[0]<>''and list2[1]<>'' and list3[2]<>'':
   if str(list1[0])==str(list2[1]) and str(list2[1])==str(list3[2]):
      if str(list1[0])=='1':
       print "Winner is player2 !!!"
      else:
       print "Winner is player1 !!!"
  if list3[0]<>'' and list2[1]<>'' and list1[2]<>'':      
   if str(list3[0])==str(list2[1]) and str(list2[1])==str(list1[2]):
      if str(list3[0])=='1':
       print "Winner is player2 !!!"
      else:
       print "Winner is player1 !!!"      
    
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
   symbol=0
   print "Will call func to update list with '0'"
   print "symbol: "+str(symbol)
   placemove(symbol,x,y,player)
  else:
   symbol=1
   print "Will call func to update list with '1'"
   print "symbol: "+str(symbol)
   placemove(symbol,x,y,player)


def listappend(symbol,listname,x,player):
 if listname[int(x)]<>0 and listname[int(x)]<>1:
   print "appending "+str(listname)
   listname[int(x)]=int(symbol)
 else:
   print "please enter new coordinates, that slot is already used"
   readmove(player)

def placemove(symbol,x,y,player):
 if int(y)==1:
  listappend(symbol,list1,x,player)
 elif int(y)==2:
  listappend(symbol,list2,x,player)
 elif int(y)==3:
  listappend(symbol,list3,x,player)
 else:
   print "Enter Valid X cordinates from 1 to 3 one more time !!! : "
   readmove(player)

 print list1
 print list2
 print list3

generatelist(list1)
generatelist(list2)
generatelist(list3)

while n<=3:
  readmove(1)
  checkmoves(list1,list2,list3)
  readmove(2)
  checkmoves(list1,list2,list3)
