import random

RPS = ["rock" , "paper" , "scissors"]

ComputerAction = random.choice(RPS)

UserAction = input("Enter a choice (rock, paper, scissors): ")

if(UserAction == ComputerAction):
    print(f"Both players selected {UserAction}. It's a tie!")

elif(UserAction == "rock" and ComputerAction == "scissors"):
    print(f"Computer_Action :  {ComputerAction}    You winn!")

elif(UserAction == "scissors" and ComputerAction == "paper"):
    print(f"Computer_Action :  {ComputerAction}    You winn!")

elif(UserAction == "paper" and ComputerAction == "rock"):
    print(f"Computer_Action :  {ComputerAction}    You winn!")

elif(UserAction == "rock" and ComputerAction == "paper"):
    print(f"Computer_Action :  {ComputerAction}    Computer winn!")

elif(UserAction == "scissors" and ComputerAction == "rock"):
    print(f"Computer_Action :  {ComputerAction}    Computer winn!")

elif(UserAction == "paper" and ComputerAction == "scissors"):
    print(f"Computer_Action :  {ComputerAction}    Computer winn!")
