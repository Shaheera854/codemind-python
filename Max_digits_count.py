def max_count(a):
    c=0
    for i in a:
        temp=i
        m=c
        c=0
        while temp:
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
    temp=i
    co=0
    while temp:
        co+=1
        temp//=10
    if co==c:
        count+=1
print(count)