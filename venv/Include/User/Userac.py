class Userac:
    def __init__(self, name, account, balance):
        self.name = name
        self.account = account
        self.balance = int(balance)


    def print_info(self):
        print("계좌번호 : ", self.account, "/ 이름 : ", self.name, " / 잔액 : ", self.balance, "원")
    
    def user_account(self):
        return self.account
    def user_balance(self):
        return self.balance
    def user_name(self):
        return self.name
    def print_balance(self):
        print("계좌잔고 : ", self.balance)
    def print_name(self):
        print("계좌잔고 : ", self.name)