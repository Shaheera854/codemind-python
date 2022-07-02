n=int(input())
a=list(map(int,input().split()))
maxi=0
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    if c==1 and maxi<i:
        maxi=i
if maxi==0:
    print("-1")
else:
    print(maxi)