def even(n):
    c=0
    while n:
        c+=1
        n//=10
    if c%2==0:
        return 1
    return 0
t=int(input())
a=list(map(int,input().split()))
c=0
for i in range(t):
    if even(a[i]):
        c+=1
print(c)