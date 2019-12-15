c=[4,6,2,6,7,3]
d=[4,5,3,2]


def Sum(a,b):
    mi=min(len(a),len(b))
    l=[]
    o1=0
    for i in range(-1,-mi-1,-1):
        k=a[i]+b[i]+o1
        o1=k//10
        o2=k%10
        l.append(o2)
    if len(a)!=len(b):
        A=len(a)
        B=len(b)
        if A>B:
            rest=a[:(len(a)-mi)]
        else:
            rest=b[:(len(b)-mi)]
        ma=max(len(a), len(b))
        for j in range(- 1, -len(rest)-1, -1):
            l.append(rest[j]+o1)
            o1=0
    l.reverse()
    return l


print(Sum(c,d))


def Dif(a,b):
    mi=min(len(a),len(b))
    l=[]
    o1=0
    c1=0
    for i in range(-1,-mi-1,-1):
        if a[i]<b[i]:
            e=a[i]+10-b[i]-c1
            c1=1
            l.append(e)
        else:
            e = a[i] - b[i] - c1
            c1 = 0
            l.append(e)
    if len(a)!=len(b):
        A=len(a)
        B=len(b)
        if A>B:
            rest=a[:(len(a)-mi)]
        else:
            rest=b[:(len(b)-mi)]
        ma=max(len(a), len(b))
        for j in range(- 1, -len(rest)-1, -1):
            l.append(rest[j]-c1)
            o1=0
    l.reverse()
    return l

print(Dif(c,d))
