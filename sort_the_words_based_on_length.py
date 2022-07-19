s=input().split()
i=0
j=1
while i<len(s) and j<len(s):
    if len(s[i])==len(s[j]):
        a1=0
        a2=0
        for k in s[i]:
            a1+=ord(k)
        for k in s[j]:
            a2+=ord(k)
        if a1>a2:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
    elif len(s[i])>len(s[j]):
        temp=s[i]
        s[i]=s[j]
        s[j]=temp
    j+=1
    i+=1
print(*s)