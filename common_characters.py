s1=input().lower()
s2=input().lower()
s=''
for i in s1:
    if i in s2 and i!=' ' and i not in s:
        s+=i
if len(s)==0:
    print("-1")
else:
    print(*sorted(list(s)),sep='')