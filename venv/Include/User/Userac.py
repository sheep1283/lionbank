class Userac:
    def __init__(self, name, account, deposit):
        self.name = name
        self.account = account
        self.deposit = deposit


    def print_info(self):
        print("계좌번호 : ", self.account, "/ 이름 : ", self.name, " / 잔액 : ", self.deposit, "원")