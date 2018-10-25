list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = []
num=int(raw_input("Enter any number :"))
for x in list:
    if x < num:
        print (int(x))
    if x < 5:
        # print ("x = "+str(x)+" which is less than 5")
        list2.append(x) 

for y in list2:
    print (str(y)+ " list of items less than 5")

#squares = [1, 4, 9, 16]
#sum = 0
#for num in squares:
#    sum +=num
#print sum
for item in reversed(list):
     print [item]
      



