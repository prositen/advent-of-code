import sys
m=lambda x:[max((n//3)-2,0) for n in x]
n=m(map(int, sys.stdin.readlines()))
s1=s2=sum(n)
while sum(n):
    n=m(n)
    s2+=sum(n)
print(s1,s2)