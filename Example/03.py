'''
03장 연습문제
https://wikidocs.net/12769#03
'''

#Q1
'''shirt'''

#Q2
i = 0
sum = 0
while i < 1000 : 
    i += 1
    if i%3 == 0 : sum += i

print(sum)

#Q3
i = 0
while i < 5 :
    i += 1
    print('*'*i)

#Q4
for i in range(1,101) :
    print(i, end=" ")

#Q5
sum = 0
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for grade in a :
    sum += grade    #점수합계
avg = sum/len(a)    #점수합계 / 학생수
print(avg)          #평균점수

#Q6
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)
