#p110
treeHit = 0
while treeHit<10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit >= 10:
        print("나무 넘어갑니다.")

#p111
number = 0
prompt = '''
1. Add
2. Del
3. List
4. Quit

Enter number: 
'''
while number != 4:
    print(prompt)
    number = int(input())

#p114
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피!")
        coffee -= 1
    elif money > 300:
        print("거스름돈 %d 그리고 커피!" % (money - 300))
        coffee -= 1
    else:
        print("돈이 부족합니다.")
        print("남은 커피의 양 %d" % coffee)
    if coffee < 1:
        print("판매 중지")
        break

#p115
a = 0
while a<10 :
    a += 1
    if a%2 == 0 : continue
    print(a)

