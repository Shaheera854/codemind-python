n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in range(n):
    s+=arr[i]
for j in range(a,b+1):
    for i in range(n):
        if arr[i]==j:
            s-=arr[i]
print(s)