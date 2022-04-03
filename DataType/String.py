'''
print("="*30)
print("String.py")
print("="*30)

a="Life is too short, You need Python"

print("-*-- 길이 --*-")
print(len(a))
print("-*-- 인덱싱 --*-")
print(a[0])
print(a[1])
print(a[-1])
print(a[-2])
print("-*-- 슬라이싱 --*-")
print(a[0:4])
print(a[5:7])
print(a[12:17])
print(a[:17])
print(a[19:])
print(a[:])
print(a[19:-7])
'''

print("-*-- 문자열 포매팅 --*-")
print("It's %d thousand won." %3)

print("-*-- format 함수 --*-")
print("I eat {0} apples".format(3))

print("-*-- format 함수 정렬 --*-")
print("{0:>10}".format("hi"))
print("{0:*^10}".format("hi"))

print("-*-- format 함수 소수점·중괄호 --*-")
print("{0:0.4f}".format(3.42134234))
print("{{ and }}".format())

print("-*-- f 문자열 포매팅 --*-")
name = '최주은'
age = '27'
print(f'이름은 {name}, 나이는 {age}.')
