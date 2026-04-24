class Account:
    def __init__(self, acc_no, acc_holder_name, balance):
        self.acc_no = acc_no
        self.acc_holder_name = acc_holder_name
        self.balance = balance

    def show_acc(self):
        print(f"Hello {self.acc_holder_name} !!")

    def showAccount(self):
        print(f"Account No: {self.acc_no}")
        print(f"Name: {self.acc_holder_name}")
        print(f"Balance: {self.balance}")

    def deposite(self, amount):
        self.balance += amount

    def windraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def aval_bal(self):
        print("Available balance:", self.balance)
