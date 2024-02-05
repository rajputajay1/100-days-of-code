from random import randint

EASY_LEVEL_TURNS =10
HARD_LEVEL_TURNS =5

def check_answer(guess,answer,turns):
    if guess>answer:
       print("Too High")
       return turns-1
    elif guess<answer:
     print("Too Low")
     return turns-1
    else:
        print(f"You got it! The answer was {answer}.")  



def check_difficulity():
    level =input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if level==  "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS    
        

def game():       
    print("Welcome to the Number Guessing Game !! ")
    answer =randint(1,100)
    # print(f"passst, the correct answer is {answer}")
    turns =check_difficulity()

    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number ")
        guess =int(input("Make a guess : "))
        turns =check_answer(guess,answer,turns)
        if turns==0:
            print("You 've run out of guesses, You Lose!")
            return
        elif guess!=answer:
            print("Guess again")


game()