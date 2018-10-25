import string
import random
policy =""
symbols=[]

def inputpolicy(policy):
 policy=int(raw_input ("Enter 1 for strong password policy, 2 for weak policy : "))
 checkvalue(policy,symbols) 

def checkvalue(policy,symbols):
 if policy == 1: 
  symbols=[]
  print ("Weak password policy selected")
 elif policy == 2:
  symbols=["@","%","&","(",")","#","*","^","~","+"]
  print ("Strong password policy selected")
 else:
  print "entered value must be 1 or 2"
  inputpolicy(policy)
#print str(symbols)

inputpolicy(policy)


dictionary=string.ascii_letters + string.digits + str(symbols)

from os import urandom
#chars = "".join([random.choice(string.letters) for i in xrange(15)])
chars = "".join([random.choice(dictionary)for i in xrange(15)])

#print (" initial chars", chars)
a=list(chars)
for i in a:
    if i == "'" or i == '"' or i == ",":
#     print "will remove this : " + str(i)   
     a.remove(i)
#     print "removed"

print ''.join(a)
