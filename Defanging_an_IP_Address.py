s=input()
s1=""
for i in range(len(s)):
    if s[i]==".":
        s1+="[.]"
    else:
        s1+=s[i]
print(s1)