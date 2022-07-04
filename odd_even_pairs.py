n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
res=[]
for i in range(n):
    if a[i]%2==0:
        e.append(a[i])
    else:
        o.append(a[i])
j=0
while j<max(len(e),len(o)):
    if j<len(o):
        res.append(o[j])
    if j<len(e):
        res.append(e[j])
    j+=1
if n%2!=0:
    res.append(0)
for i in res:
    print(i,end=' ')