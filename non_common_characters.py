s1=input()
s2=input()
s1=s1.replace(' ','')
s2=s2.replace(' ','')
s1=str.lower(s1)
s2=str.lower(s2)
s=[]
for i in s1:
    if i not in s2 and i:
        s.append(i)
for i in s2:
    if i not in s1:
        s.append(i)
s=set(s)
s=list(s)
s=sorted(s)
print(*sorted(s),sep='')