s=input()
s=str.lower(s)
s=s.split()
a=[]
s1=s[0]
for i in s1:
    c=0
    for j in s:
        if i in j:
            c+=1
    if c==len(s) and i not in a:
        a.append(i)
if len(a)==0:
    print('-1')
else:
    m=a[0]
    for i in range(1,len(a)):
        m=min(m,a[i])
    print(m)