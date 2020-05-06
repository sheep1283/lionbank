class Account :
    def deposit(self, money):
        self.balance += money
        return self.balance

    def withdraw(self, money):
        self.balace -= money
        return money