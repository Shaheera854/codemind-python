n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]=abs(a[i])
a=sorted(a)
for i in range(n):
    print(a[i]**2,end=" ")