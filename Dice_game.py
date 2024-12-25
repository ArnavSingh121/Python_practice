import random

player1 = input("Your Name: ")
player2 = input("Your Name: ")
player3 = input("Your Name: ")
player4 = input("Your Name: ")

player1_total = 0
player2_total = 0
player3_total = 0
player4_total = 0


condition_met = False  # Flag to track if any condition is met



while not condition_met:

    
    dice_roll1 = random.randint(1,12)
    dice_roll2 = random.randint(1,12)
    dice_roll3 = random.randint(1,12)
    dice_roll4 = random.randint(1,12)
    
    player1_total += dice_roll1
    player2_total += dice_roll2
    player3_total += dice_roll3
    player4_total += dice_roll4
    
    print("Player 1 total: ", player1_total)
    print("Player 2 total: ", player2_total)
    print("Player 3 total: ", player3_total)
    print("Player 4 total: ", player4_total)
    
    if player1_total >= 100:

      condition_met = True

      print(player1, "Wins!")

      break
    
    elif player2_total >= 100:

        condition_met = True

        print(player2, "Wins!")

        break

    elif player3_total >= 100:

        condition_met = True

        print(player3, "Wins!")

        break

    elif player4_total >= 100:

        condition_met = True

        print(player4, "Wins!")

        break
    
    else: 
       continue


# store dice roll for player 1 and check to see if the value is equal to 100, if it is, end game, if not, move to player 2
# Do same thing again, roll and store for player 2, check the value, continue if not 100, Same for 3 and 4.
# If loop or boolean for checking conditions to check each value to make sure that the total doesnt exceed 100
# change into game once all elements work. 




