import string
import random

word_list = ["pencil","book","library","newspaper","university","computer","weather","city","country","notebook","gun"]
random.shuffle(word_list)
x = random.choice(word_list)

choise_list = ["_"]*len(x)

i=1
while i <7:
    if i <6:
        user_input =input("Write a letter: ")
        if user_input in x:
            for m, harf in enumerate(x):
                if harf == user_input:
                    choise_list[m] = user_input
            print("Correct")
            print(choise_list)
        else:
            print(f"Invalid Input. You have {6-i} attempts left")
        i = i+1
    elif i == 6:
        print("This is your last chance.")
        last_attempt = input("Write the true word: ")
        if last_attempt == x:
            print("You Win".center(30,"*"))
        else:
            print("You Lose")
        i = i+1



