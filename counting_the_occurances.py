s=input()
t=input()
c=0
for i in range(len(s)):
   if s[i] in t:
       c+=1
if c>0:
    print(c)
else:
    print("-1")