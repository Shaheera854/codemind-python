n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in range((a.index(k))+1):
   s+=a[i]
print(s)