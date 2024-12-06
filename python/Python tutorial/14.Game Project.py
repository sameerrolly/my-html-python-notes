# rock paper secisor
import random

print("Choose between rock, paper, scissors")
computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Enter your choice: ").lower()

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice  == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")


