fi='SOMIN.INP'
fo='SOMIN.OUT'
with open(fi)as f:
    n=int(f.readline())
    a=list(map(int,f.read().split()))
with open(fo,'w')as f:
    if 0<=n<=10**6 and 0<max(a)<=10**9:
            d=[]
            for i in range(n):
                if a[i] != (i+1):
                    print(i+1,file=f)
                    break
