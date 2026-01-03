print("Welocome To The Calculator")

def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def square(a):
    return a ** 2
def cube(a):
    return a ** 3
def divide(a,b):
    if b ==0:
        return "Cannot divide by zero"
    return a/b


calculator = {
    "+" : plus,
    "-" : minus,
    "*" :multiply,
    "/" :divide,
    "^" :square,
}

first_number = int(input("Enter the first number: "))
while True:
    choice = input("What would you like to do?(+,-,*,/,^): ")
    if choice == "^":
        result = calculator[choice](first_number)
    elif  choice in calculator.keys():
        second_number = int(input("Enter the second number: "))
        result = calculator[choice](first_number,second_number)
    else:
        print("Invalid choice")
        continue
    print(f"Result = {result}")

    query = input("Do you want to continue?(Yes,No): ").lower()
    if query == "Yes":
        continue
    else:
        print("Goodbye")
        break


