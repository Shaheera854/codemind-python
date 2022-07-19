s=input()
s1=''
s=s.replace(' ','')
for i in s:
    c=0
    for j in s:
        if i==j or ord(i)+32==ord(j) or ord(i)-32==ord(j) and i!=' ' and j!=' ':
            c+=1
    if c==1:
        s1+=i
print(*sorted(str.lower(s1)),sep='')