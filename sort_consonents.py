n=list(map(str,input().split()))
s=''
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in n:
    l=list(i)
    for x in range(len(l)):
        for y in range(len(l)):
            if x!=y and l[x] not in vowels and l[y] not in vowels and l[x]<l[y]:
                temp=l[x]
                l[x]=l[y]
                l[y]=temp
    print(*l,sep='',end=' ')
    