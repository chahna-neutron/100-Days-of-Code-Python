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
game_images=[rock,paper,scissors]
user_num=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))
if(user_num>=0 and user_num<=2):
    print("You chose:\n")
    print(game_images[user_num])
a=random.randint(0,2)
print("Computer chose")
print(game_images[a])
if(user_num>2 and user_num<0):
    print("You typed an invalid number, you lose!!!")
elif(user_num==0 and a==1):
    print("you lose!")
elif(user_num==1 and a==2):
    print("you lose!")
elif(user_num==2 and a==0):
    print("you lose!")
elif(user_num==a):
    print("DRAW!!")
elif(user_num==0 and a==2) :
    print("you win!")
elif(user_num==1 and a==0) :
    print("you win!")
elif(user_num==2 and a==1) :
    print("you win!")