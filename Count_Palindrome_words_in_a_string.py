st=input()
st=st.lower()
st=st.split()
c=0
for i in st:
    rev=i[-1::-1]
    if rev==i:
        c+=1
print(c)