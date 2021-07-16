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
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_input<=2:
  Game=[rock,paper,scissors]
  user_choice=(Game[user_input])
  print(user_choice)

  import random
  computer_input = random.randint(0,2)
  computer_choice = Game[computer_input]
  print(computer_choice)

  if computer_choice==user_choice:
    print("It is draw!")
  if computer_choice!=user_choice:
    winner = rock > scissors or scissors > paper or paper > rock
    if winner == "True":
      print("You lost")
    else:
      print("You are the winner")
  
else:
  print("You entered a wrong input")
