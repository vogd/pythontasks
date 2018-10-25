import random
a = random.sample(range(100),10)
#print len(a)
print a

def slist(x):
 b =[x[0],x[len(x)-1]]
 print b

slist(a)
