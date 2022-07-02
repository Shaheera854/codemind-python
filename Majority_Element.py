n=int(input())
a=list(map(int,input().split()))
b=set(a)
maxi=0
me=0
for i in b:
    c=0
    for j in a:
        if i==j:
            c+=1
    if maxi<c:
        maxi=c
        me=i
print(me)