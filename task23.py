mylist1=[]
mylist2=[]
resultlist=[]
import os
dir = os.getcwd()

file1=dir+"/primenumbers.txt"
file2=dir+"/happynumbers.txt"

def readfile(file1,mylist1):
  with open(file1,"r") as f:
   item=f.readline() 
   while item:
    #print item
    mylist1.append(int(item))
    item=f.readline()
  print "\n File elements from " + file1  
  print mylist1
  return mylist1

readfile(file1,mylist1)
readfile(file2,mylist2)

resultlist=set(mylist1)&set(mylist2)

print "\n Result list of elements presented in both files"
print sorted(resultlist)
