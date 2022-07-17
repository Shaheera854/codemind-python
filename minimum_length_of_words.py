s=input()
s=s.split()
m=len(s[0])
for i in range(1,len(s)):
    m=min(m,len(s[i]))
print(m)