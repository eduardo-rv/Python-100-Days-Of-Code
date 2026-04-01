import random

lst = ["Rock", "Paper", "Scissors"]

choose = lst[int(input("0.Rock\n1. Paper\n2. Scissors\nWhat do you choose? "))]
computer = lst[random.randint(0,2)]

if (choose == computer):
    print("You Tie")
    print(f"Yuo {choose} vs Computer {computer}")

elif (choose == "Rock" and computer == "Scissors"):
    print("You Win")
    print(f"Yuo {choose} vs Computer {computer}")

elif (choose == "Scissors" and computer == "Rock"):
    print("You Lose")
    print(f"Yuo {choose} vs Computer {computer}")

elif (choose == "Rock" and computer == "Paper"):
    print("You Lose")
    print(f"Yuo {choose} vs Computer {computer}")

elif (choose == "Paper" and computer == "Rock"):
    print("You Win")
    print(f"Yuo {choose} vs Computer {computer}")

elif (choose == "Paper" and computer == "Scissors"):
    print("You Lose")
    print(f"Yuo {choose} vs Computer {computer}")

elif (choose == "Scissors" and computer == "Paper"):
    print("You Win")
    print(f"Yuo {choose} vs Computer {computer}")

else:
    print("Error")
    print(f"Yuo {choose} vs Computer {computer}")
