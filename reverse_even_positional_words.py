s=input()
s=s.split()
for i in range(0,len(s),2):
    s[i]=s[i][::-1]
print(*s)