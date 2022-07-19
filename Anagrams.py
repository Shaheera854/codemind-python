s1=input()
s2=input()
s1=str.lower(s1)
s2=str.lower(s2)
if len(s1)==len(s2):
    for i in s1:
        if i not in s2:
            print(False)
            break
    else:
        print(True)
else:
    print(False)