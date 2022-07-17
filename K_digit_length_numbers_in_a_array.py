n,k=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in a:
    temp=abs(i)
    co=0
    while temp:
        co+=1
        temp//=10
    if i==0:
        co+=1
    if co==k:
        count+=1
print(count)