s1=input().lower()
s2=input().lower()
s=''
for i in s1:
    if i in s2 and i!=' ' and i not in s:
        s+=i
print(len(s))