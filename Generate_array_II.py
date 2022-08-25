n=int(input())
a=list(map(int,input().split()))
a1=[]
for i in range(0,n-1,2):
    for j in range(a[i+1]):
        a1.append(a[i])
print(*a1)