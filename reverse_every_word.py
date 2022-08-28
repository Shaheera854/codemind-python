n=input().split()
l=[]
for i in n:
    l.append(i[-1::-1])
print(*l)