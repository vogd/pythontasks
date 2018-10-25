num = int(raw_input("Enter a digit :"))
i=0
listresult=[]
while  i < 100:
 x=num*i
 listresult.append(x)
 i=i+1

print(listresult)


#----How should be----

listrange=list(range(1,num+1))
divisorlist=[]

for number in listrange:
    if num % number == 0:
        divisorlist.append(number)

print (divisorlist)
