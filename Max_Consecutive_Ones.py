n=int(input())
a=list(map(int,input().split()))
maxi=0
c=0
for i in range(n):
    if a[i]==1:
        c+=1
        maxi=max(maxi,c)
    else:
        c=0
print(maxi)