num=int(raw_input("Enter amount of fibo items : "))
list1=[1,1]
for i in range(1,(num-1)):
    list1.append(list1[i]+list1[i-1])
    print list1

