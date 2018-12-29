import sys
reverse=[]
counter=0

word=raw_input("enter a palindrome word : ") 
e=int(len(word))
#print reversed(word)
#sys.exit()
i=e

while int(i)>0:
 i=i-1
 reverse.append(word[i])
print "reversed word "+str(reverse)

for n in range(e):
 if reverse[n]==word[n]:  
  counter=int(counter+1)
if counter>0:
 print "PALINDROME !!!"
else:
 print "NOOO"


