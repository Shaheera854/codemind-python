s=input().lower().split()
vowels='aeiouAEIOU'
maxi=0
for i in s:
    c=0
    for j in range(len(i)):
        if i[j] in vowels:
            c+=1
    print(c,end=' ')