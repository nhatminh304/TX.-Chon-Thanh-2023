fi='MAX.INP'
fo='MAX.OUT'
with open(fi)as f:
    n=int(f.readline())
    k=int(f.read())
    b=[int(i) for i in str(n)]
with open(fo,'w')as f:
    l= len(b)
    if 2<=l<=255 and k<l:
        b=sorted(b)
        del b[k:] #[2, 3, 5, 5]
        for i in str(n):
            if int(i) not in b:
                print(i,end='',file=f)
    
