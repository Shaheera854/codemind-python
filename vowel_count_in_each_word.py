def count(i):
    v=['a','e','i','o','u','A','E','I','O','U']
    c=0
    for j in range(len(i)):
        if i[j] in v:
            c+=1
    return c
s=input().split()
for i in s:
    print(count(i),end=' ')