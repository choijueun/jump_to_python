#선언
s1 = set()
s2 = set([1,2,3])
s3 = set("Hello Python")


a = set([1, 2, 3, 4, 5])
b = set([1, 3, 5, 7, 9])

#교집합
a & b
a.intersection(b)
#합집합
a | b
a.union(b)
#차집합
a - b
a.difference(b)