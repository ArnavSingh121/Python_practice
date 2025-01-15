import random
    
while True: 

    choice = int(input("1 - Rock, 2 - Paper, 3 - Scissors >> ")) # takes input from the user for their pick
    
    while choice > 3 or choice < 1: # Check for validity of the input
        choice = int(input('Enter a valid choice please: '))
        
    if choice == 1:
        choice_name = "Rock"
        
    elif choice == 2:
        choice_name = "Paper"
    
    else:
        choice_name = "Scissors"
        
        
    print("User chose >> ", choice_name)
   
    
    print("Computers turn")
    

    choice_2 = random.randint(1,3)

    if choice_2 == 1:
        choice_name_2 = "Rock"
    
    elif choice_2 == 2:
        choice_name_2 = "Paper"

    elif choice_2 == 3:
        choice_name_2 = "Scissors"
    
    print("Computer chose >> ", choice_name_2)


    #Draw
    if (choice == choice_2):
        print("Its a Draw!")

    elif(choice == 1 and choice_2 == 3):
     print("User wins!")
     
    elif(choice_2 == 1 and choice == 3):
      print("Computer wins!")
      
    elif(choice == 1 and choice_2 == 2):
     print("Computer wins!")
     
    elif(choice_2 == 1 and choice == 2):
      print("User wins!")
    
    elif(choice == 2 and choice_2 == 3):
     print("Computer wins!")
     
    elif(choice_2 == 2 and choice == 3):
      print("User wins!")
      
      
    print("Do you want to play again? (Y/N) >> ")
     
    restart = input()
    
    if restart == "Y" or restart == "y":
        continue
    else:
        break
    
print("Thank you for playing!")
    

    
    

    
    



