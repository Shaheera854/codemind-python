p,r,t=input().split()
p=float(p)
r=float(r)
t=float(t)
ci=p*pow((1+r/100),t)
print('{:.2f}'.format(ci))