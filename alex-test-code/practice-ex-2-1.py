class BankAccount:
    def __init__(self):
        self.name = 'My bank account'
        self.balance = 0

    def display(self):
        print(self.name, self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

ba1 = BankAccount()

ba1.display()
ba1.deposit(100)
ba1.display()