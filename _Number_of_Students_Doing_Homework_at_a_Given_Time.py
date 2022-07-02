m=int(input())
st=list(map(int,input().split()))
n=int(input())
et=list(map(int,input().split()))
qt=int(input())
c=0
for i in range(n):
    for j in range(st[i],et[i]+1):
        if j==qt:
            c+=1
            break
print(c)