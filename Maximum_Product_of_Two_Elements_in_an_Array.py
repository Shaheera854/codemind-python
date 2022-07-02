a=list(map(int,input().split()))
maxi=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        x=(a[i]-1)*(a[j]-1)
        maxi=max(maxi,x)
print(maxi)