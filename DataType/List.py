#선언
list_a = []
list_b = list()
list_c = [1,3,5,7,9]
list_d = ['Life', 'is', 'too', 'short']
list_e = [1,2,['You', 'need', 'Python']]

#인덱싱
list_c[2]
list_c[0]+list_c[4]

#슬라이싱
list_e[1:]
list_e[2][1:3]

#연산
#더하기
a = [1,2,3]
b = [4,5,6]
a+b

#반복하기
a*3

#길이 구하기
len(a)

#수정하기
a[2] = 4

#삭제하기
b = [1,2,3,4,5]
del b[2]
print(b)
del b[2:]
print(b)

#복사하기
a = [1, 2, 3, 4]
b = a[:]
from copy import copy
c = copy(a)

a[1] = 4
print(a)
print(b)
print(c)