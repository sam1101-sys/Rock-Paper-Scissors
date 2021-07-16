rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input<=2:
  Game=[rock,paper,scissors]
  user_choice=(Game[user_input])
  print(user_choice)

  import random
  computer_input = random.randint(0,2)
  computer_choice = Game[computer_input]
  print(f"Computer choose\n {computer_choice}")

  if user_input == 0 and computer_input == 2:
    print("You win!")
  elif computer_input == 0 and user_input == 2:
    print("You lose")
  elif computer_input > user_input:
    print("You lose")
  elif user_input > computer_input:
    print("You win!")
  elif computer_input == user_input:
    print("It's a draw")
  
else:
  print("You entered a wrong input")
