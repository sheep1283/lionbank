import User.Userac as user

if __name__=="__main__":
    #내용이 User.Userac typedls 리스트
    userlist=[]
    #초기 화면, 입력 받을 화면
    print("======Back Menu=====\n", "1. 계좌개설\n", "2. 입금하기\n", "3. 출금하기\n", "4. 전체조회\n", "5. 프로그램 종료\n",
          "===================")
    num = int(input("입력 : "))
    #5입력시까지 계속 반복
    while num !=5:

        if(num == 1):
            print("======계좌개설======")
            accnum = input("계좌번호 : ")
            name = input("이름 : "),...
            depo = input("예금 : ")
            #입력받은 계좌, 이름, 예금 정보를 User.Userac 클래스에 입력하고, 입력 정보를 accnum에 저장(여기서 accnum의 type은 char에서 해당 클래스의 type으로 바뀜)
            accnum = user.Userac(name, accnum, depo)
            #userlist에 생성된 유저 정보 저장(이름, 계좌, 예금)
            userlist.append(accnum)
            print("##계좌개설을 완료하였습니다##\n", "==================")
        elif(num == 2):
            print("2")
        elif(num == 3):
            print("3")
        elif(num == 4):
            #userlist의 크기(저장된 사람수)로 for문 돌려 0번째부터 userlist의 크기번째까지 모두 출력
            for i in range(len(userlist)):
                userlist[i].print_info()
        else:
            print("다시 입력해주세요")

        print("======Back Menu=====\n", "1. 계좌개설\n", "2. 입금하기\n", "3. 출금하기\n", "4. 전체조회\n", "5. 프로그램 종료\n",
              "===================")
        num = int(input("입력 : "))
    print("##프로그램을 종료합니다##")