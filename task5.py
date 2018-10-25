import random
count1 = int(random.randint(4,8))
count2 = int(random.randint(4,8))
print ("list1 length :" +str(count1))
print ("list2 length :"+str(count2))
a=random.sample(range(1,10),int(count1))
b=random.sample(range(1,10),int(count2))

c=[]
print (str(a))+(str(b))
for x in a:
    if x in b:
        if x in c:
            print ("Item " + str(x)+ " already in list. Skipping")
        else:  
          c.append(x)
print (c)
