# import random
# print('ROCK PAPER SCISSORS GAME')

# user_choice =int(input('what do you chose ? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))
# computer_choice =random.randint(0,2)
# print(f"computer choice {computer_choice}")
# if user_choice>=3 or user_choice<0:
#     print('You enterd invalid number You lose.')
# elif user_choice==0 and computer_choice==2:
#     print('You win')
# elif user_choice == 2 and computer_choice == 0:
#     print('computer Win')
# elif computer_choice>user_choice:
#     print('computer Win')
# elif computer_choice < user_choice:
#     print('You Win!')
# elif computer_choice==user_choice:
#     print('Match is draw!')
# total =0
# for number in range(2 ,101,2):
# #  print(number)
#  total+=number
# print(total)

total =0
for i in range(1 ,11):
    if i%2==0:
        total+=i
print(total)