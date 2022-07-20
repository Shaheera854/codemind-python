m,n=map(int,input().split())
a=[]
for i in range(m):
    x=list(map(int,input().split()))
    a.append(x)
se=0
so=0
for i in range(m):
    for j in range(n):
        if a[i][j]%2==0:
            se+=a[i][j]
        else:
            so+=a[i][j]
print(se,so)