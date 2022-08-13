n=int(input())
a=list(map(int,input().split()))
for i in range(1,n-1):
    if (a[i]>a[i-1] and a[i]<a[i+1]) or (a[i]<a[i-1] and a[i]>a[i+1]):
        print("no")
        break
else:
    print("yes")