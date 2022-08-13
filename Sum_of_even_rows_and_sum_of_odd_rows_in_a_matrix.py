m,n=map(int,input().split())
l=[]
for i in range(m):
    a=list(map(int,input().split()))
    l.append(a)
se=0
so=0
for i in range(m):
    for j in range(n):
        if i%2==0:
            se+=l[i][j]
        else:
            so+=l[i][j]
print(se,so)