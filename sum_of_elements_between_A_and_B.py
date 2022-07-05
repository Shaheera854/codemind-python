n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in range(a,b+1):
    for j in range(n):
        if arr[j]==i:
            s+=arr[j]
print(s)