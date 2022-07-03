s=input()
s1='0123456789'
c=0
for i in range(len(s)):
    if s[i] in s1:
        c+=1
if c>0:
    print("Contains",c,"digit")
else:
    print("Doesn't contain digit")