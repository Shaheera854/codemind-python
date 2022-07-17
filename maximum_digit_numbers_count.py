def max_count(a):
    c=0
    for i in a:
        temp=abs(i)
        m=c
        c=0
        while temp!=0:
            c+=1
            temp//=10
        if c<m:
            c=m
    return c
n=int(input())
a=list(map(int,input().split()))
c=max_count(a)
count=0
for i in a:
    temp=abs(i)
    co=0
    while temp!=0:
        co+=1
        temp//=10
    if co==c:
        print(i,end=' ')