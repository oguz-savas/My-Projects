from pathlib import Path
import os
from datetime import datetime



user_path = Path('/Users/oguzsavas/Desktop/PythonProject/ex/Diary.txt')

print("Welcome To The Diary Program")



while True:
    user_choice = input("Please Choose One Of The Options(1-Read The Diary, 2- Add New Note, 3-Exit)(Write Only Numbers): ")
    if user_choice == "1":
        with open(user_path, "r") as file:
            print(file.read())
        query = input("Do you want to continue? (yes/no)").lower()
        if query == "yes":
            print("Ok. Program is restarting again.")
            continue
        else:
            break
    elif user_choice == "2":
        now = datetime.now()
        formatted = now.strftime("%d.%m.%Y %H:%M:%S")
        user_passage = input("Please Enter Your Passage: ")
        diary_passage = "\n" + formatted + "\n" + user_passage
        with open(user_path, "a", encoding="utf-8") as f:
            f.write(diary_passage)
        query = input("Do you want to continue? (yes/no)").lower()
        if query == "yes":
            print("Ok. Program is restarting again.")
            continue
        else:
            break
    elif user_choice == "3":
        break


print("Ok. Program is shutting down.")
print("Ok. Goodbye")

