t=int(input())
for j in range(t):
    s=input()
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':
            print("Yes")
            break
    else:
        print("No")