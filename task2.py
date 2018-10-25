num=int(raw_input("Enter any digit:"))
divider=int(raw_input("enter divider: "))

result=int(num) % 2
fourresult=int(num) % 4
check=int(num) % int(divider)

#print(result)
if result == 0:
    print ("number "+ str(num)+ " even")
else:
    print ("number " +str(num)+ " is uneven")

if fourresult == 0:
    print (str(num)+" number is a multiple of 4")

if check == 0:
    print ("Num " +str(num)+ " divided evenly with divider " +str(divider))
else:
    print ("Num " +str(num)+" does not divide evenly with divider "+str(divider) )

