from Account import Account

class Savingacc(Account):
    def __init__(self, acc_no, acc_holder_name, balance, min_bal):
        super().__init__(acc_no, acc_holder_name, balance)
        self.min_bal = min_bal

    def windraw(self, amount):
        if self.balance - amount >= self.min_bal:
            self.balance -= amount
            print("Withdrawal successful (Saving)")
        else:
            print("Minimum balance must be maintained")

    def aval_bal(self):
        print("Available balance:", self.balance - self.min_bal)