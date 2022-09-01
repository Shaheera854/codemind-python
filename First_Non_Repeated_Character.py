t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    l=list(s)
    l1=[]
    for j in l:
        if l.count(j)==1:
            l1.append(j)
    if len(l1)==0:
        print("-1")
    else:
        print(l1[0])