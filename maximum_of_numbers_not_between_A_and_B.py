n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
for i in range(a,b+1):
    l1.append(i)
l2=[]
for i in range(0,n):
    if l[i] not in l1:
        l2.append(l[i])
if len(l2)==0:
    print("-1")
else:
    print(max(l2))