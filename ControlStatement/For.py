#p117
import re


test_list = ['You', 'need', 'Python']

for i in test_list :
    print(i)

#p118
a = [(1, 2), (3, 4), (5, 6)]

for (i, j) in a :
    print(i+j)

#p118
marks = [90, 25, 67, 45, 80]
number = 0
for grade in marks :
    number += 1
    if grade>60 :
        print("%d번 학생은 합격입니다." %number)
    else :
        print("%d번 학생은 불합격입니다." %number)

#p121
add = 0
for i in range(1,11) :
    add += i
    print("i의 값: %d" %i)
print("1부터 10까지의 합계: %d" %add)

#p121
marks = [90, 25, 67, 45, 80]
for num in range(len(marks)) :
    if marks[num] < 60 :
        continue
    print("%d번 학생 합격입니다." %(num+1))

#p122
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print ('')

#p123
a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)

result = [num*3 for num in a if num%2 == 0]
print(result)

gugu = [i*j for i in range(2,10)
            for j in range(1,10)]
print(gugu)