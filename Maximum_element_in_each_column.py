m,n=map(int,input().split())
a=[]
mat=[]
for i in range(m):
     a.append(list(map(int,input().split())))
for j in range(n):
    maxi=0
    for i in range(m):
        maxi=max(maxi,a[i][j])
    print(maxi)