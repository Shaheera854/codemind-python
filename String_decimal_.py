t=int(input())
for j in range(t):
    s=input()
    for i in range(len(s)):
        if not(s[i]>="0" and s[i]<="9"):
            print(False)
            break
    else:
        print(True)