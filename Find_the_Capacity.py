t,s,b=map(int,input().split())
c=2*t*s*b*512
ckb=c//1024
print("{}KB".format(ckb))