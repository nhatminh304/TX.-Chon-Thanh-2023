fi='KITUDT.INP'
fo='KITUDT.OUT'
with open(fi)as f:
    n=int(f.readline())
    a=f.read()
with open(fo,'w')as f:
    if 0<n<=10**6 and len(a) <=10**6:
        b=[i for i in a] #['a', 'b', 'c', 'd', 'b', 'c']
        for i in a:
            if b.count(i) == n:
                kq=b.index(i)+1
                print(kq,file=f)
                break
        else:
            print(-1,file=f)
