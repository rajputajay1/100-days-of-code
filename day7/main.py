import random
word_list =["ardvark","baloon","camel","rose","monkey"]

chose_word =random.choice(word_list)
print(f"Psst the solution {chose_word}")
# guess =input("guess a letter : ").lower()
display =[]
lives =6
for _ in range(len(chose_word)):
    display += "_"
print(display)
end_of_game =False
while not  end_of_game:
    guess =input("guess a letter : ").lower()
    if guess in display:
        print(f"You've already guessed :{guess} ")
    for position in range(len(chose_word)):
        letter =chose_word[position]
        if letter == guess:
            display[position]=letter
    if guess not in chose_word:
        # print(guess)
        print(f"You guessed {guess},that's not in the word. You lose a life {lives} ")
        lives-=1
        if lives==0:
            end_of_game =True
            print('You lose.')
    print(f"{' '.join(display)}")
    if "_" not in display:
     end_of_game =True
     print("You Win")

print(f"word is :  {chose_word}")