n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]==0:
        print(a[i],end=" ")
for i in range(n):
    if a[i]==1:
        print(a[i],end=" ")