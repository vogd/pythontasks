# Download file and read random word from it
#import os
#os.system ("wget -Nnc http://norvig.com/ngrams/sowpods.txt")

counter=0
uplimit=0
import os
import sys
import urllib

urllib.urlretrieve("http://norvig.com/ngrams/sowpods.txt", os.getcwd()+"/sowpods.txt")
#print os.getcwd()
#limit=int(os.popen("wc -l sowpods.txt | awk -F' ' '{print$1}'").read())
#print limit
#sys.exit()

with open('sowpods.txt','r') as f:
 line=f.readline()
 while line:
   counter=int(counter+1)    
   line=f.readline()
 print "Total lines in file : "+ str(counter)
 from random import *
 linetoread=randint(1,int(counter))
 print "Need to print line number : "+str(linetoread)
 line=open('sowpods.txt','r').readlines()[linetoread]
 print line
print "All lines are read"
