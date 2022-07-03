s=input()
c=0
for i in range(len(s)):
    if s[i]>='0' and s[i]<='9':
        c+=int(s[i])
print(c)