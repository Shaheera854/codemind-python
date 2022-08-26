n=input().lower().split()
l=[]
for j in range(len(n[0])):
    c=0
    i=0
    while i<len(n):
        if n[0][j] in n[i]:
            c+=1
        else:
            break
        i+=1
    if c==len(n):
        l.append(n[0][j])
if len(l)==0:
    print("-1")
else:
    print(min(l))