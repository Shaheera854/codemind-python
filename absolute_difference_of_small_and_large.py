n=input().split()
s_min=0
s_max=0
for i in n:
    mini=ord(i[0])
    maxi=ord(i[0])
    for j in range(1,len(i)):
        if mini>ord(i[j]) and i[j].isalnum():
            mini=ord(i[j])
        if maxi<ord(i[j]) and i[j].isalnum():
            maxi=ord(i[j])
    print(abs(mini-maxi),end=' ')