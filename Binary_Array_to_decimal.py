n=int(input())
a=list(map(int,input().split()))
j=n-1
s=0
for i in range(n):
    s+=(a[i]*pow(2,j))
    j-=1
print(s)