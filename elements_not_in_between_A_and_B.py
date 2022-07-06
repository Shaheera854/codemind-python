n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for j in range(a,b+1):
    for i in arr:
        if j==i:
            arr.remove(i)
if len(arr)>0:
    for i in arr:
        print(i,end=' ')
else:
    print("-1")