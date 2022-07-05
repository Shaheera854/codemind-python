n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
maxi=0
for i in range(a,b+1):
    for j in range(n):
        if arr[j]==i:
            maxi=max(maxi,arr[j])
if maxi>0:
    print(maxi)
else:
    print("-1")