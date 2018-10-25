a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]
for item in a:
     if item % 2 ==0:
       b.append(item)

print (b)     

c=[element for element in a if element % 2 ==0]
print (c)
