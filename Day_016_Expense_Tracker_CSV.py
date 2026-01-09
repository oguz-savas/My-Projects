import csv
import os

desktop_path = r'/Users/oguzsavas/Desktop'
file_path = r'/Users/oguzsavas/Desktop/expense_tracker.csv'

def saving_expenses():
    spending_category = input("What category do you want your expenses? ")
    spending_amount = float(input("What is the amount of spending? "))

    file_exists = os.path.exists(file_path)

    with open(file_path, mode="a", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([spending_category, spending_amount])

        if not(file_exists):
            writer.writerow(["category", "spending_amount"])

        writer.writerow([spending_category, spending_amount])

def reading_expenses():
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

def analyse_expenses():
    fix_csv_if_needed()

    total = 0.0
    try:
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row["spending_amount"] == "spending_amount":
                    continue  # header satırını atla

                total += float(row["spending_amount"])
    except FileNotFoundError:
        print("Any sepndings yet.")

    print("Total expenses:", total)


def fix_csv_if_needed():
    with open(file_path, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()

    if first_line != "category,spending_amount":
        lines = []
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("category,spending_amount\n")
            f.writelines(lines)


print("Welcome to the expense tracker!")

while True:
    query = input("What do yo want? (save/read/analyze/exit): ").lower()
    if query == "save":
        saving_expenses()
        continue
    elif query == "read":
        reading_expenses()
        continue
    elif query == "analyze":
        #fix_csv_if_needed()
        analyse_expenses()
        continue
    elif query == "exit":
        break
print("Goodbye!")




