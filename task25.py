import random

guessedlist=[50]

flag=0 

def generatenum(guessed,guessednew,guessedlist):
  n= int(len(guessedlist)-1) # because n> than actual item numbers since index starts from 0
  if int(guessed) < int(guessednew):
    print str(guessed)+" < "+ str(guessedlist[n-1]) 
    print "range to generate from "+str(guessed)+" to "+str(guessednew)
    guessed =random.randrange(guessed,guessednew)
  else :
    print str(guessed)+ " > "+ str(guessednew)
  # if the next guessed < than your num
    print "range to generate from "+str(guessednew)+" to "+str(guessed)
    guessed =random.randrange(guessednew,guessed)
  print ("Guessed generated "+str(guessed))
  guessnum ("Enter 'o' if guessed 'y' if the number is bigger than your guessed and 'n' if not: ",guessed)
def guessnum(text,guessed):
  global flag
  print guessed
  confirmation = str(raw_input(text))
  flag==0
  while (flag==0):
   if confirmation =="o":
    print ("Congrats! You have guessed the number !!!!")
    guessedlist.append(guessed)
    print ("We have used " + str(len(guessedlist))+ " attempts to guess your number.")
    flag==1
    raise SystemExit
   elif confirmation=="y":
    guessedlist.append(guessed)
    guessednew=abs(guessed-(guessed/2))
    print "next number range is up to "+str(abs(guessed-(guessed/2)))
    print "Failed attempts so far " +  str(len(guessedlist))
    while guessed>0:
     generatenum(guessed,guessednew,guessedlist) # if the newlygeneratednum depending on customer input is bigger/or smaller we need to generate from smaller numbers array then
   else:
    guessedlist.append(guessed)
    guessednew=abs(guessed+(guessed/2))
    print "next number range is up to "+str(guessed)
    print "Failed attempts so far " +  str(len(guessedlist))
    generatenum(guessed,guessednew,guessedlist) # if the num is smaller , then we need to generate from between last bigger numbers array and currently generated


guessnum("Enter 'o' if guessed 'y' if the number is bigger than your guessed and 'n' if not: ",100/2)


