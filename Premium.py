from Savingacc import Savingacc

class Premium(Savingacc):
    def __init__(self, acc_no, acc_holder_name, balance, min_bal):
        super().__init__(acc_no, acc_holder_name, balance, min_bal)

        if self.balance < 10000:
            print("Minimum 10000 required for Premium Account")
        else:
            print("Premium Account Activated!")

    def windraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful (Premium)")
        else:
            print("Insufficient balance")

    def show_benefits(self):
        print("Premium Benefits:")
        print("- Priority service")
        print("- No minimum balance restriction")
