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

import random
userinp = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
compinp = random.randint(0,2)
list1 = [rock,paper,scissors]
if(userinp == 0 and compinp == 2) :
  outcome = 0
elif(userinp == 1 and compinp == 0):
  outcome = 0
elif(userinp == 2 and compinp == 1):
  outcome = 0
elif(userinp == compinp):
  print(list1[userinp])
  print("Computer chose: ")
  print(list1[compinp])
  print("It's a draw.")
  exit(0)
elif(userinp > 2 or userinp < 0):
  print("You chose wrong number, you lose.")
  exit(0)
else :
  outcome = 1

if outcome == 0 :
  print(list1[userinp])
  print("Computer chose: ")
  print(list1[compinp])
  print("You win.")
elif outcome == 1 :
  print(list1[userinp])
  print("Computer chose: ")
  print(list1[compinp])
  print("You lose.")
