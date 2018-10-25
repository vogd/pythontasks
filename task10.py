import random
from sets import Set
x=[]
a = Set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
b = Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

#x = a.intersection(b)
x=a & b
   # x.append(i)
for i in x:
 print(i)
