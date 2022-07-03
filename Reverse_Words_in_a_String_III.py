s=input()
s1=""
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
s1=s1.split(" ")
for i in range(len(s1)-1,-1,-1):
    print(s1[i],end=" ")