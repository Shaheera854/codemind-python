n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
if a<b:
    for i in range(a,b+1):
        if i in l:
            l1.append(i)
else:
    for i in range(b,a+1):
        if i in l:
            l1.append(i)
if len(l1)==0:
    print("-1")
else:
    print(max(l1))