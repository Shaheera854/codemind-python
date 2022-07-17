def max_count(s):
    s=s.split()
    v=['a','e','i','o','u','A','E','I','O','U']
    c=0
    for i in range(len(s)):
        m=c
        c=0
        for j in range(len(s[i])):
            if s[i][j] in v:
                c+=1
        if c<m:
            c=m
    return c
s=input()
print(max_count(s))