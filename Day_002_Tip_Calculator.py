print("Welcome to the Tip Calculator!")
bill = float(input("What Is The Total Amount Of The Bill?: "))
tip = int(input("What percentage tip would you like to give? (10, 12, or 15):  "))
num_of_person = int(input("How many person share the bill?:  "))

calc_the_bill =  (bill + (bill * tip/100) ) / num_of_person
print(f"Amount Per Person: {calc_the_bill:.2f}")

