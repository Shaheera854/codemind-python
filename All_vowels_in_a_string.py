s=input()
vowels1='aeiou'
vowels2='AEIOU'
c=0
for i in vowels1:
    if i not in s:
        c=1
        break
else:
    print(True)
if c==1:
    for i in vowels2:
        if i not in s:
            print(False)
            break
    else:
        print(True)