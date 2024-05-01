import random

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

RPS = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissor : "))
if player == 0:
    print(RPS[0])
elif player == 1:
    print(RPS[1])
elif player == 2:
    print(RPS[2])
else:
    print("Invalid Input")

print("Computer Choose : ")
computer = random.randint(0, 2)
print(RPS[computer])

if player == computer:
    print("Draw")
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("You Won")
else:
    print("You Lose")
