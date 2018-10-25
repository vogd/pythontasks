def get_integer(text):   
# return int(raw_input(text))
 while True:
  try:
   return int(raw_input(text))
   break
  except ValueError:
   print "Oops!  That was no valid number.  Try again..."


num = get_integer("Enter integer :")

divisorlist = []


for i in range(1,num+1):
    if num % i == 0:
     divisorlist.append(i)
print(divisorlist)

def divisor_def(i):
 if int(len(divisorlist)) == 2:
    print("Number entered is not even")
 else:
    print ("Number is even")

divisor_def(i)


#----How should be----

# listrange=list(range(1,num+1))
# divisorlist=[]

# for number in listrange:
#    if num % number == 0:
#     divisorlist.append(number)
# print (divisorlist)
