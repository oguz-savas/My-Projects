from pathlib import Path
import os
from datetime import datetime



user_path = Path('/Users/oguzsavas/Desktop/PythonProject/ex/Diary.txt')

print("Welcome To The Diary Program")
user_choice = input("Please Choose One Of The Options(1-Read The Diary, 2- Add New Note, 3-Exit)(Write Only Numbers): ")


if user_choice == "1":
    with open(user_path, "r") as file:
        print(file.read())
elif user_choice == "2":
    now = datetime.now()
    formatted = now.strftime("%d.%m.%Y %H:%M:%S")
    user_passage = input("Please Enter Your Passage: ")
    diary_passage = "\n" + formatted +"\n" + user_passage
    with open(user_path, "a", encoding = "utf-8") as f:
        f.write(diary_passage)
elif user_choice == "3":
    print("Ok. Goodbye")
