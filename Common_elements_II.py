m,n=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a=[]
for i in a1:
    if i not in a2 and i not in a:
        a.append(i)
for i in a2:
    if i not in a1 and i not in a:
        a.append(i)
print(*a)