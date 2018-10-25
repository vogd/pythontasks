import random
a=random.randint(0,10)
i=1

while i > 0:
 userinput = raw_input("Enter Guessed value (enter 'exit' for exit): ")
 if userinput == "exit":
  exit(0)
 else: 
  if int(userinput) in range (1,10):
   if int(userinput) == a:
    print ("Congrats !!! You Guessed the digit from " +str(i) + " attempts!")
    exit(0)
   else:
    print ("Wrong...Please try again...")   
    i=i+1 
  else:
   print("enter value between 0 and 9")

