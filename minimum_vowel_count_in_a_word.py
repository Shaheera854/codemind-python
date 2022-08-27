s=input().lower().split()
vowels='aeiouAEIOU'
mini=0
for i in s:
    c=0
    for j in range(len(i)):
        if i[j] in vowels:
            c+=1
    if mini==0 or mini>c:
        mini=c
print(mini)