import random

options = ["stone", "paper", "scissors"]

compchoice = random.choice(options)

userchoice = input("Choose between scissors, paper and stone: ")

print("Computer's choice is: " + compchoice)

if userchoice == compchoice:
  print("It's a tie!")
elif userchoice == "stone" and compchoice == "scissors":
  print("You win!")
elif userchoice == "paper" and compchoice == "stone":
  print("You win!")
elif userchoice == "scissors" and compchoice == "paper":
  print("You win!")
else:
  print("You lose!")