def asum(n):
    temp=n
    add=0
    while temp:
        r=temp%10
        add+=r
        temp//=10
    return add
n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    s+=asum(a[i])
print(s)