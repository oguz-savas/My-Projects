

class BankAccount:
    def __init__(self,owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f" ${amount} has been deposited. Current balance: {self.balance} ")

    def withdraw(self,amount):
        self.balance -= amount
        print(f" ${amount} has been withdrawn. Current balance: {self.balance} ")
    def display_balance(self):
        print(f" {self.owner}'s balance: {self.balance} ")

account1 = BankAccount("Oğuz")
while True:
    print("Welcome to Banking System")
    print("1.Deposit, 2.Withdraw,3. Display Balance, 4.Exit")
    query = input("Your choice(1/2/3/4/): ")

    if query == "1":
        deposit_amount = float(input("Enter the amount to deposit: "))
        account1.deposit(deposit_amount)
        continue
    elif query == "2":
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        account1.withdraw(withdraw_amount)
        continue
    elif query == "3":
        account1.display_balance()
        continue
    else:
        break
print("Thank you for using Banking System")
