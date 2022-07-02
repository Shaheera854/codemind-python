n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] and a[j] and i!=j and a[i]==a[j]:
            c+=1
            a[i]=0
            a[j]=0
            break
print(c)