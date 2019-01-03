a=[1,1,2,3,4,3,5,2,5,3,4,7,7,6,5,8,9,9,0,7,8,0,1]
#print set(a)

b=[]

for i in a: 
 if i not in b:
  b.append(i)

print b
