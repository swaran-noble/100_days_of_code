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

options = [rock, paper, scissors]
our_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if our_choice>=0 and our_choice<=2:
    print(options[our_choice])   

computer_choice = random.randint(0,2)
print("Computer chose:\n")
print(options[computer_choice])

if our_choice>2 or our_choice<0:
    print("You chose a wrong number.You lose")
elif our_choice==computer_choice:
    print("It's a draw!")
elif our_choice==0 and computer_choice==2:
    print("You win!")
elif our_choice==2 and computer_choice==0:
    print("You lose!")
elif our_choice<computer_choice:
    print("You lose!")
elif our_choice>computer_choice:
    print("You win!")        



