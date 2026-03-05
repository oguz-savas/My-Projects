import json

print("Welcome to password manager.")

# Dosya yoksa boş liste oluştur
try:
    with open("data.json", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

while True:
    use_input = input("What Do you wanna use?: Add /Look/Exit ").lower()

    if use_input == "add":
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        new_data = {"email": email, "password": password}
        data.append(new_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    elif use_input == "look":
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                print(data)
        except FileNotFoundError:
            print("No data found.")

    elif use_input == "exit":
        print("Thank you for using the password manager.")
        break

    else:
        print("Invalid input.")

