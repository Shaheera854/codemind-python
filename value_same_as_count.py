n=int(input())
a=list(map(int,input().split()))
a1=[]
for i in a:
    if i not in a1:
        a1.append(i)
t=0
for i in range(len(a1)):
    if a.count(a1[i])==a1[i]:
        t+=1
print(t)