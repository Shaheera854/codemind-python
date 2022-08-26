n=int(input())
a=list(map(int,input().split()))
a1=list(set(a))
s=0
c=0
for i in range(len(a1)):
    if a.count(a1[i])==a1[i]:
        s+=a[i]
        c+=1
if s==0:
    print("-1")
else:
    print("{:.2f}".format(s/c))