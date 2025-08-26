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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [ rock , paper , scissor]

player = int(input('Choose any "0 for rock" "1 for paper" "2 for scissor". \n'))
if player >= 0 and player <=2:
    print(list[player])

random_list = random.randint(0 , 2)

print(list[random_list])
if player >= 3 or player <0:
    print("Invalid No. You Lose")
elif random_list == player:
    print("Its Draw!")
elif random_list == 0 and player == 2 or random_list == 1 and player == 0 or random_list == 2 and player == 1:
    print("You Loss!")
elif player == 0 and random_list ==2 or player == 1 and random_list == 0 or player == 2 and random_list == 1:
    print("You Win!")
