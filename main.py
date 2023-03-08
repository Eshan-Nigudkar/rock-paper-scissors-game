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


user = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
data_a = [rock, paper, scissors]
import random

random_no = random.randint(0, 2)
print(f"You choose {data_a[user]}")
print(f"Computer chooses {data_a[random_no]}")
if (user == 0 and random_no == 2):
    print("You win!")
if (user == 2 and random_no == 1):
    print("You win!")
if (user == 1 and random_no == 0):
    print("You win!")
elif (user == 2 and random_no == 2):
    print("That's a tie!")
elif (user == 1 and random_no == 1):
    print("That's a tie!")
elif (user == 2 and random_no == 2):
    print("That's a tie!")
elif (user >= 3):
    print("That's a invalid number! You lost!")
else:
    print("You lost!")
