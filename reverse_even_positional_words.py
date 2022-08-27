n=input().split()
l1=[]
for i in range(len(n)):
    if i%2==0:
        l1.append(n[i][-1::-1])
    else:
        l1.append(n[i])
print(*l1)