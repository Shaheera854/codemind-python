s=input().split()
for k in s:
    a=list(k)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j] and a[i] not in 'aeiou' and a[j] not in 'aeiou':
                a[i],a[j]=a[j],a[i]
    print(*a,sep='',end=' ')