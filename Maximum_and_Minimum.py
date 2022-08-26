n=int(input())
a=list(map(int,input().split()))
a1=list(set(a))
a2=[]
for i in range(len(a1)):
    if a.count(a1[i])==a1[i]:
        a2.append(a1[i])
if len(a2)==0:
    print("-1")
else:
    print(min(a2),max(a2))