string=str(raw_input("enter string :"))
forward=[]
backward=[]
i = 0
i2 = 0
for c in string:
     forward.append(c)
for d in reversed(forward):
      backward.append(d)

# backward = forward[::-1]



if cmp(forward,backward) == 0:
    print ("Lists are palindromes")


print ("backward :" +str(forward))
print ("backward :" +str(backward))

