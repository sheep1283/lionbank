import User.Userac as user

if __name__=="__main__":
    userlist=[]
    print("======Back Menu=====\n", "1. 계좌개설\n", "2. 입금하기\n", "3. 출금하기\n", "4. 전체조회\n", "5. 프로그램 종료\n",
          "===================")
    num = int(input("입력 : "))
    while num !=5:

        if(num == 1):
            print("======계좌개설======")
            accnum = input("계좌번호 : ")
            name = input("이름 : ")
            depo = input("예금 : ")
            accnum = user.Userac(name, accnum, depo)
            userlist.append(accnum)
            print("##계좌개설을 완료하였습니다##\n", "==================")
        elif(num == 2):
            print("2")
        elif(num == 3):
            print("3")
        elif(num == 4):
            for i in range(len(userlist)):
                userlist[i].print_info()
        else:
            print("다시 입력해주세요")

        print("======Back Menu=====\n", "1. 계좌개설\n", "2. 입금하기\n", "3. 출금하기\n", "4. 전체조회\n", "5. 프로그램 종료\n",
              "===================")
        num = int(input("입력 : "))
    print("##프로그램을 종료합니다##")