n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
l=[]
for i in range(a,b+1):
    l.append(i)
for i in arr:
    if i in l:
        print(i,end=' ')
        s=1
if s!=1:
    print("-1")