n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
mini=100
for i in range(a,b+1):
    for j in range(n):
        if arr[j]==i:
            if mini>0:
                mini=min(mini,arr[j])
if mini!=100:
    print(mini)
else:
    print("-1")