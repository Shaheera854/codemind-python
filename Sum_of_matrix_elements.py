m=int(input())
n=int(input())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
s=0
for i in range(m):
    for j in range(n):
        s+=a[i][j]
print(s)