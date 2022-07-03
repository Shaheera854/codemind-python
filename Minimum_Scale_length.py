n=int(input())
a=list(map(int,input().split()))
min=a[0]
count=0
for i in range(n):
    if min>a[i]:
        min=a[i]
while min:
    count=0
    for j in range(n):
        if a[j]%min==0:
            count+=1
    if count==n:
        print(min)
        break
    min-=1