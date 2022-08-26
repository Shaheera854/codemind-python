n=int(input())
a=list(map(int,input().split()))
f=[]
l=[]
for i in range((n//2)+1):
    if n%2==0 and i==n//2:
        break
    f.append(a[i])
    if i!=n//2:
        l.append(a[n-i-1])
i=0
j=0
while i<len(f) or j<len(l):
    if i<len(f):
        print(f[i],end=' ')
        i+=1
    if j<len(l):
        print(l[j],end=' ')
        j+=1
if n%2!=0:
    print("0")