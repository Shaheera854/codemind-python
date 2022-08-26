n=list(map(str,input().split()))
for i in n:
    l=list(i)
    for x in range(len(l)):
        for y in range(len(l)):
            if x!=y and l[x].isalnum() and l[y].isalnum() and l[x]<l[y]:
                temp=l[x]
                l[x]=l[y]
                l[y]=temp
    print(*l,sep='',end=' ')