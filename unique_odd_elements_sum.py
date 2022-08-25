n=int(input())
a=list(map(int,input().split()))
s=0
a=set(a)
a=list(a)
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j]:
            c+=1
    if c<=1 and a[i]%2!=0:
        s+=a[i]
print(s)