import random
flag = 1
choice = ['empty','rock','paper','scissors']

while flag > 0:
    usr_command = raw_input("Hit Enter to Start Game")
    
    usr_name1 = raw_input("Enter User1 name : ")
    m1 = int(raw_input(" enter choice 1-rock, 2-paper, 3-scissors: "))
    if m1 not in range (1,4):
     print("Error numeric values from 1 to 3 only")
    else: 
    
     usr_name2 = raw_input("Enter User2 name : ")
     m2 = int(raw_input(" enter choice 1-rock, 2-paper, 3-scissors: "))
     if m2 not in range (1,4):
      print("Enter numeric values from 1 to 3 only")
     else: 
      game = int(random.randint(1,3))
      print (game)
      if choice[m1] == choice[game]:
       print ("Winner is User1 " + choice[game])
      else:
       if choice[m2] == choice[game]:
        print ("Winner is User2 " + choice[game])
       else:
        print ("its a draw..")   
