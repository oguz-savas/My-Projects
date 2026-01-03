import random

easy_level_turns = 10
hard_level_turns = 5

answer = random.randint(0,100)

def check_answer(guess,answer,turns):
    if guess == answer:
        print("You got it!")
        return True
    elif guess > answer:
        print("Too high!")
    else:
        print("Too low!")
    return False

print("Weolcome To The Guess Game")
level_num = input("Difficulty Level(hard/easy): ")
if level_num == "hard":
    level_of_guess = hard_level_turns
else:
    level_of_guess = easy_level_turns
print("You have " + str(level_of_guess) + " turns left.")

guess_num = level_of_guess
while guess_num > 0:
    guess_num = guess_num - 1
    guess = int(input("Guess: "))
    if check_answer(guess,answer,level_of_guess):
        break
    print("You have " + str(guess_num) + " turns left.")


if guess != answer:
    print("You've run out of guesses. You lose.")


