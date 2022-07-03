n=int(input())
a=list(map(int,input().split()))
hcf=a[0]
for i in range(1,n):
    while hcf!=a[i]:
        if hcf>a[i]:
            hcf-=a[i]
        elif hcf<a[i]:
            a[i]-=hcf
print(hcf)