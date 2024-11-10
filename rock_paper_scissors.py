import random
ran=['rock','paper','scissors']
while True:
    player=input("Enter Your Choice [rock,paper or scissors]:").lower()
    pc=random.choice(ran)
    if pc=='rock' and player=='paper':
        print("You've Won!")
    elif pc=='rock' and player=='scissors':
        print("You've Lost!")
    elif pc=='paper' and player=='rock':
        print("You've Lost!")
    elif pc=='paper' and player=='scissors':
        print("You've Won!")
    elif pc=='scissors' and player=='rock':
        print("You've Won!")
    elif pc=='scissors' and player=='paper':
        print("You've Lost!")
    elif pc==player:
        print("Its A Draw")
    else:
        print("Invalid Choice")
    play_again=input("Do You Want to continue[y/n]:").lower()
    if play_again =='n':
        print("Thank You Playing!!!")
        break