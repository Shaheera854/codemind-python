n=int(input())
a=list(map(int,input().split()))
a1=[]
for i in a:
    if i not in a1:
        a1.append(i)
for i in range(len(a1)):
    print(a1[i],a.count(a1[i]),end=' ')