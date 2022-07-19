s=input()
s=list(s)
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]>s[j] and s[i] not in '!@#$%^&*(){}[]''"":;/?.>,<\|+=-_ ' and s[j] not in '!@#$%^&*(){}[]''"":;/?.>,<\|+=-_ ':
            s[i],s[j]=s[j],s[i]
print(*s,sep='',end=' ')