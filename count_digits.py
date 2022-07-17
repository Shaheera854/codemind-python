n=int(input())
a=list(map(int,input().split()))
for i in a:
    temp=abs(i)
    co=0
    while temp:
        co+=1
        temp//=10
    if i==0:
        co+=1
    print(co,end=' ')