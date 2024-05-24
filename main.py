import random

print("Welcome to Rock, Paper, Scissors!")

user_input = input("What is your move? (rock, paper, scissor)")
print("You picked: " + user_input)
computer_choice = random.choice(["rock",'paper',"scissors"])
print("The computer picked: " + computer_choice)

if user_input == "rock":
  if computer_choice == "scissors":
    print("You win! :)")
  elif computer_choice == "paper":
    print("You lose! :(")
  else:
    print("it's a draw :|")
elif user_input == "scissors":
  if computer_choice == "paper":
    print("You win! :)")
  elif computer_choice == "rock":
    print("You lose! :(")
  else:
    print("it's a draw :|")
elif user_input == "paper":  
  if computer_choice == "rock":
    print("You win! :)")
  elif computer_choice == "scissors":
    print("You lose! :(")
  else:
    print("it's a draw :|")
else:
  print("You didn't make a valid choice")