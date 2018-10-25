import random

a=random.sample(range(15),10)
b=random.sample(range(15),10)
 
print a
print b

def remover(a,b):
    [b.remove(i) for i in b if i in a]   
    [a.remove(z) for z in a if z in b]
    c=a+b
    printer(c)
    
def printer(x):
 print x
     
remover(a,b)

