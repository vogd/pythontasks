import os
mylist=[]
dir=os.getcwd()
print (dir) 

def openfile2(myfile):
 with open(myfile) as f:
  #read file and strip end of line symbols while file is read
  content = f.readline()
  while content:
   mylist.append(content.strip())  
   content=f.readline()
  print mylist

# List Separate list with Uniq items
 uniq = set(mylist)
 print uniq 
 # strip values from end of symbol values
 #uniq = [elem.strip().split(',')for elem in uniq]
 for elem in uniq:
      num=mylist.count(elem)
      print str(elem) +":"+ str(num)    

myfile = dir+"/nameslist.txt"
openfile2(myfile)

