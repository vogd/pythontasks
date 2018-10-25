import random
x=int(raw_input("How many fibonacci digits to store :"))
list_d =[1,1]

def append(list_d,x):
 while len(list_d)<=x-1:   
  d=int(list_d[-1]+list_d[-2])
  list_d.append(d)

append(list_d,x)
print (list_d)
