import random

ran_no=random.randint(1,100)
chance = 5
while chance > 0:
    no=int(input("Guess A Number Between (1-100):"))
    if no > ran_no:
        print("The Number You've Guessed is high")
    elif no < ran_no:
        print("The Number You've Guessed is low")
    elif no == ran_no:
        print("The Number You've Guessed is Correct")
        break
    else:
         print("Please enter a valid number!")
    chance = chance-1
    if chance == 0:
        print("You've Lost Try Again")
        


