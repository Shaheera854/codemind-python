s=input()
mvc=ord(s[0])
for i in range(1,len(s)):
    mvc=max(mvc,ord(s[i]))
print(chr(mvc))