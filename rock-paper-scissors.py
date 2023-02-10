import random

weapons = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(weapons)
    user = None
    while user not in weapons:
        user = input("Choose between rock, paper and scissors :").lower()

    if user == computer:
        print("No winner!")

    elif user == 'rock':
        if computer == "paper":
            print("computer has won!")
        elif computer == "scissors":
            print("user has won!")

    elif user == 'paper':
        if computer == "rock":
            print("user has won!")
        elif computer == "scissors":
            print("computer has won!")

    elif user == 'scissors':
        if computer == "paper":
            print("user has won!")
        elif computer == "rock":
            print("computer has won!")
    print("--------------------------")
    print(f"Computer : {computer}")
    print(f"User :{user}")
    print("--------------------------")
    more_round = input("Do you want to play one more round ? (y/n)").lower()
    if more_round != "y":
        break
print("Have a good day!")
