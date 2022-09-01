n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
for i in range(a,b+1):
    l1.append(i)
maxi=0
for i in range(n):
    if l[i] not in l1 and maxi<l[i]:
        maxi=l[i]
if maxi==0:
    print("-1")
else:
    print(maxi)