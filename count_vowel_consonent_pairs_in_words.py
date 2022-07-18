s=input().split()
vowels=['a','e','i','o','u','A','E','I','O','U']
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
c=0
for k in s:
    i=0
    j=len(k)-1
    while i<(len(k)//2) and j>=(len(k)//2):#shaheera
        if k[i] in vowels and k[j] in consonants:
            c+=1
        elif k[i] in consonants and k[j] in vowels:
            c+=1
        i+=1
        j-=1
print(c)
