s1=input().lower()
s2=input().lower()
s=''
for i in s1:
    if i not in s2 and i!=' ':
        s+=i
for i in s2:
    if i not in s1 and i!=' ':
        s+=i
s=set(s)
print(len(s))