fi='KHEPKIN.INP'
fo='KHEPKIN.OUT'
with open(fi)as f:
    n=f.read()
with open(fo,'w')as f:
    if 1<=int(n)<=10**10:
        s=0
        for i in n:
            if int(i)==0 or int(i)==4 or int(i)==6 or int(i)==9:
                s+=1
            elif int(i)==8:
                s+=2
        print(s,file=f)