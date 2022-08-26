n=int(input())
a=list(map(int,input().split()))
a1=[]
for i in a:
    if i not in a1:
        a1.append(i)
print(*a1)