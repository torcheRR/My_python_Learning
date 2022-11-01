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
choices=[rock,paper,scissors]
your_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
your_digit=choices[int(your_choice)]
print(your_digit)
print("Computer chose:")
computer_choise=random.randint(0,2)
computer_digit=choices[computer_choise]
print(computer_digit+"\n")
if (your_choice==2 and computer_choise==1) or (your_choice==0 and computer_choise==1) or (your_choice==1 and computer_choise==2):
    print("You lose!")
elif your_choice==computer_choise:
    print("Draw!")
elif (your_choice==2 and computer_choise==1) or (your_choice==0 and computer_choise==2) or (your_choice==1 and computer_choise==0):
    print("You win!")