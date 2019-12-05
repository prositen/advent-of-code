import sys
m=lambda x:[max((n//3)-2,0)for n in x]
n=m(map(int,sys.stdin.readlines()))
a=b=sum(n)
while sum(n):
    n,b=m(n),sum(n)+b
print(a,b)