s1=input()
s2=input()
s1=s1.replace(' ','')
s2=s2.replace(' ','')
s1=str.lower(s1)
s2=str.lower(s2)
s=[]
for i in s1:
    if i in s2 and i not in s:
        s.append(i)
if len(s)==0:
    print('-1')
else:
    print(*sorted(s),sep='')