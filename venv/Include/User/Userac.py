class Userac:
    def __init__(self, name, account, deposit):
        self.name = name
        self.account = account
        self.deposit = int(deposit)


    def print_info(self):
        print("계좌번호 : ", self.account, "/ 이름 : ", self.name, " / 잔액 : ", self.deposit, "원")
    
    def user_account(self):
        return self.account
    def print_name(self):
        print("계좌이름 : ", self.name)
    def print_deposit(self):
        print("계좌잔고 : ", self.deposit)