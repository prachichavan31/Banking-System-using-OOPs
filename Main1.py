from Account import Account
from Savingacc import Savingacc
from Premium import Premium

print("\n--- Welcome to Banking System ---")

print("\nChoose Account Type:")
print("1. Normal Account")
print("2. Saving Account")
print("3. Premium Account (Recommended)")

choice = int(input("\nEnter your choice: "))

acc_no = int(input("\nEnter account number: "))
acc_holder_name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))


if balance >= 10000 and choice != 3:
    print("\nYou are eligible for Premium Account!")
    print("We recommend Premium for better benefits.")

if choice == 1:
    user = Account(acc_no, acc_holder_name, balance)

elif choice == 2:
    min_bal = int(input("Enter minimum balance: "))
    user = Savingacc(acc_no, acc_holder_name, balance, min_bal)

elif choice == 3:
    min_bal = int(input("Enter minimum balance (for record): "))
    user = Premium(acc_no, acc_holder_name, balance, min_bal)

else:
    print("Invalid choice")
    exit()

print("\n--- Banking Operations ---")
deposit = int(input("Enter deposit amount: "))
withdraw = int(input("Enter withdraw amount: "))

user.deposite(deposit)
user.windraw(withdraw)
user.aval_bal()

if choice == 3:
    user.show_benefits()

print("\nThank you for using Banking System..Have a Good day!")