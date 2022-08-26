n=int(input())
a=list(map(int,input().split()))
k=int(input())
a1=[]
for i in a:
    if i not in a1:
        a1.append(i)
t=0
for i in range(len(a1)):
    if a.count(a1[i])==k:
        print(a1[i],end=' ')
        t=1
if t==0:
    print("-1")