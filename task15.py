x=raw_input(str("enter words : "))
word_list =x.split (' ')
i=0

def split_string(string):
  letters=list(string)
  letters.reverse()
  print letters

def reverse(list_a,i):
 while i <= len(list_a)-1:   
  i=i+1
  string=list_a[-i]
  print string 
  split_string(string) 

reverse(word_list,i)

