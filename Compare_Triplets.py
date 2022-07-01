a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a=[0,0]
for i in range(3):
    if a1[i]>a2[i]:
        a[0]+=1
    elif a1[i]<a2[i]:
        a[1]+=1
print(a[0],a[1])