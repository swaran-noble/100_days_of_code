from art import logo
import random


EASY_CHANCES = 10
HARD_CHANCES = 5


def check_answer(guess_number, actual_number, chance):
    if guess_number<actual_number:
        print("Too low\n")
        chance-=1
        return chance
    elif guess_number>actual_number:
        print("Too high\n")
        chance-=1
        return chance
    else:
        print(f"You got it! The answer was {actual_number}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level=='easy':
        return EASY_CHANCES
    else:
        return HARD_CHANCES

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100:")
    number = random.randint(1,100)

    turns = set_difficulty()

    guess = 0

    while guess!=number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,number,turns)
        if turns == 0:
            print("You've run out of guesses,you lose.")
            return
        elif guess!=number:
            print("Guess again.")


game()            







