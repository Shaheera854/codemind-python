n=input()
n=n.lower()
s=''
for i in n:
    if i!=' ':
        s+=i
print(*sorted(set(s)),sep='')