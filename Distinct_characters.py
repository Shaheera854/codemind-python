s=input()
s=s.lower()
l=[]
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[i]==s[j] and s[i]!=' ':
            c+=1
    if c==1:
        l.append(s[i])
l=sorted(l)
for i in l:
    print(i,end='')