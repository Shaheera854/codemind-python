n=int(input())
a=list(map(int,input().split()))
t=0
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    if c==1:
        print(i,end=" ")
        t=1
if t!=1:
    print("-1")