m,n=map(int,input().split())
a=[]
for i in range(m):
    x=list(map(int,input().split()))
    a.append(x)
s=0
for i in range(m):
    for j in range(n):
        s+=a[i][j]
print(s)