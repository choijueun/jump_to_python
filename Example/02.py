'''
02장 연습문제
https://wikidocs.net/12769#02
'''

#Q1
avg = (80+75+55)/3
print(avg)

#Q2
if 13%2 == 1:
    print("홀수")
else:
    print("짝수")

#Q3
hong = '881120-1068234'
print(hong[:6])
print(hong[7:])

#Q4
print(hong[7])

#Q5
a = "a:b:c:d"
print(a.replace(":", "#"))

#Q6
list_Q6 = [1,3,5,4,2]
list_Q6.sort(reverse=True)
print(list_Q6)

#Q7
str_Q7 = ['Life', 'is', 'too', 'short']
print(' '.join(str_Q7))

#Q8
set1 = (1,2,3)
set2 = (4,)
set3 = set1 + set2
print(set3)

#Q9
a = dict()
'''
1. a['name'] = 'python'
2. a[('a',)] = 'python'
3. a[[1]] = 'python'
→ 리스트는 Key로 사용 불가
4. a[250] = 'python'
'''

#Q10
a = { 'A':90, 'B':80, 'C':70 }
print(a['B'])
print(a.get('B'))

a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)            # {'A':90, 'C':70} 출력
print(result)       # 80 출력

#Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = list(set(a))
print(b)

#Q12
'''
a = b = [1, 2, 3]
a[1] = 4
print(b)
: [1, 4, 3]
'''