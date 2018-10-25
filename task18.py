import random

def generatedigit():
 x= random.randint(0,9999)
 print x
 get_integer ("Guess a 4 digit number ",x,cows,bulls)

y=""
cows = 0
bulls = 0
inputl=[]

def get_integer(text,x,cows,bulls):
 while True:
  try:
   y=int(raw_input(text))
   inputl = list(str(y))
   if len(inputl)<4:
    print ("Please, Enter 4 digit value")
   elif len(inputl)>4:
    print ("Please, Enter a 4 digit value") 
  # print ("Y is "+str(y))
   else:
    cowscheck(y,x,cows,bulls)
  except ValueError:
   print "Oops!  That was no valid number.  Try again..."

def cowscheck(y,x,cows,bulls):
 #print x
 #print y
 if x == y:
  cows = cows+1
  print ("You guessed!!!!")
  print ("You have "+str(cows)+" cows.")
  raise SystemExit
 else:
  bulls=bulls+1
  print ("Boo")
  print ("You have " + str(bulls) + " bulls.")
  get_integer("Guess a 4 digit number one more time :",x,cows,bulls)

generatedigit()
