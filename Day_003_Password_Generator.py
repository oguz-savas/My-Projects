import string
import random

word = "Welcome To The Password Generator"
final_word = word.center(30,"-")
print(final_word)


letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

password_generator = []

num_of_letter = int(input("How many letters would you like to generate?: "))
num_of_symbol = int(input("How many symbols would you like to generate?: "))
num_of_number = int(input("How many numbers would you like to generate?: "))

for i in random.sample(letters, num_of_letter):
    password_generator.append(i)
for i in random.sample(numbers, num_of_number):
    password_generator.append(i)
for i in random.sample(symbols, num_of_symbol):
    password_generator.append(i)

random.shuffle(password_generator)
final = "".join(password_generator)
print(f"Your Password: {final}")

if len(final) < 8:
    print("Your password is too weak.")
elif 8<= len(final) <=12:
    print("Your password is good enough.")
else:
    print("Your password is too strong.")
