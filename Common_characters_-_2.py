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
    if c==len(s):
        a.append(i)
print(len(a))