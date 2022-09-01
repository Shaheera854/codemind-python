n=input()
l=list(n)
for i in l:
    if l.count(i)>1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")