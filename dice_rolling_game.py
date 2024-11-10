import random

while True:
    choice=input("Do You Want to Play (y/n):").lower()
    if choice == 'y':
        result=random.randint(1,6),2
        print(result)
    elif choice == 'n':
        print("Thanks For Playing")
        break
    else:
        print("Inavalid Input!")
