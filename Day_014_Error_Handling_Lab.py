print("Wwlcome To Number Sum Game")
while True:
    try:
        user_numbers = input("Enter numbers separated by comma: ")
        user_numbers = user_numbers.split(",")
        numbers = [float(n.strip()) for n in user_numbers]
        if any(n < 0 for n in numbers):
            raise ValueError("Negative numbers are not allowed")
        user_sum = sum(numbers) / len(numbers)

    except ValueError as e:
        print(f"Entry Error: {e}")
    except ZeroDivisionError:
        print("Error: You didn't enter a valid number")
    else:
        print("The sum is", user_sum)
    finally:
        query = input("Do you want to continue? (yes/no)").lower()
        if query == "yes":
            print("Ok. Program is restarting again.")
            continue
        else:
            print("Program Ended")
            break









