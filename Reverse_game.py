def reverse(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    return rev
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    print(reverse(a[i]),end=' ')