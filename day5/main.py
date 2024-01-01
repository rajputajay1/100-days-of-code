# # import  random
# # letterss =['a','b','c','d', 'e', 'f', 'g', 'h', '1', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
# # numbers =['0','1','2','3','4','5','6','7','8','9']
# # symbol =['@','#','$','%','^','&','*','(',')','+']

# # # easy level
# # letter =int(input("How many Letters would you like in your password ?:"))
# # sym =int(input('How many Symbal would you like ?:'))
# # num =int(input('How many Number would you like ?:'))
# # password =""
# # for char in range(1,letter+1):
# #     password +=random.choice(letterss)
# # for char in range(1,sym+1):
# #     password +=random.choice(numbers)
# # for char in range(1,num+1):
# #     password +=random.choice(symbol)
# #     print("Generated Password:", password)


#     # hard level

# import  random
# letterss =['a','b','c','d', 'e', 'f', 'g', 'h', '1', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
# numbers =['0','1','2','3','4','5','6','7','8','9']
# symbol =['@','#','$','%','^','&','*','(',')','+']

# letter =int(input("How many Letters would you like in your password ?:"))
# sym =int(input('How many Symbal would you like ?:'))
# num =int(input('How many Number would you like ?:'))
# password_list =[]
# for char in range(1,letter+1):
#     password_list.append(random.choice(letterss))
# for char in range(1,sym+1):
#     password_list +=random.choice(numbers)
# for char in range(1,num+1):
#     password_list +=random.choice(symbol)
#     # print(password_list)
#     random.shuffle(password_list)
#     # print(password_list)
#     password =""
# for char in password_list:
#     password+=char
#     print("Generated Password:", password)

import random

letterss = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

password_length = int(input("How many characters would you like in your password?: "))

all_chars = letterss + numbers + symbol

password = ''
for i in range(password_length):
    password += random.choice(all_chars)

print("Generated Password:", password)
