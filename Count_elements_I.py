m,n=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a1=set(a1)
a2=set(a2)
c=0
for i in a1:
    if i in a2:
        c+=1
print(c)