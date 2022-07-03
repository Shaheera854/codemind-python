t=int(input())
for j in range(t):
    s=input()
    s1=""
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    if s==s1:
        print("YES",end=" ")
        if len(s)%2==0:
            print("EVEN")
        else:
            print("ODD")
    else:
        print("NO")