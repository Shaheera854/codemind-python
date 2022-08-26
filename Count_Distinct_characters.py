s=input()
s=s.lower()
s1=''
for i in s:
    if i!=' ':
        s1+=i
s1=list(s1)
print(len(set(s1)))