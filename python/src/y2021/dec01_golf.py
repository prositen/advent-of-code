import sys
n=[*map(int,sys.stdin.readlines())]
for i in 1,3:
    print(sum(a<b for a,b in zip(n,n[i:])))