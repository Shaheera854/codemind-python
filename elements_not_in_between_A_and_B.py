n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
for i in range(a,b+1):
    l1.append(i)
t=0
for i in range(n):
    if l[i] not in l1:
        print(l[i],end=' ')
        t=1
if t==0:
    print("-1")