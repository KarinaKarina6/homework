#Здесь ввод
f="H6 G1 H8"

ff=f.split()
f1=ff[0]
f2=ff[1]
f3=ff[2]


letters=["A","B","C","D","E","F","G","H"]
digits=["1","2","3","4","5","6","7","8"]


def hodi_korol(x):
    b1=chr(ord(x[0])+1)
    b2=x[0]
    b3=chr(ord(x[0])-1)
    ts1=str(int(x[1])+1)
    ts2=x[1]
    ts3=str(int(x[1])-1)
    p=[b1,b2,b3]
    B=[]
    for i in p:
        if i in letters:
            B.append(i)
    t=[ts1,ts2,ts3]
    TS=[]
    for i in t:
        if i in digits:
            TS.append(i)
    res=[]
    for i in B:
        for j in TS:
            res.append(i+j)
    res.remove(x)
    return res


def hodi_ladia(x):
    p1=x[0]
    p2=x[1]
    res=[]
    for i in letters:
        res.append(i+p2)
    for i in digits:
        res.append(p1+i)
    res.remove(x)
    return res


def func(x,y,z):
    c = list(set(hodi_korol(x)) & {z}) # король атакует короля?
    d=list(set(hodi_ladia(y)) & {z}) # атакует ли ладья?
    e=list(set(hodi_ladia(y)) & set(hodi_korol(z))) # может ли уйти от ладьи?
    g=list(set(hodi_korol(x)) & set(hodi_korol(z))) # может ли уйти от короля?
    if c!=[]:
        return "Strange"
    elif d!=[] and list(set(hodi_korol(z))-set(e)-set(g))!=[]:
        return "Check"
    elif d!=[] and list(set(hodi_korol(z))-set(e)-set(g))==[]:
        return "Checkmate"
    elif d==[] and list(set(hodi_korol(z))-set(e)-set(g))!=[]:
        return "Norma"
    elif d==[] and list(set(hodi_korol(z))-set(e)-set(g))==[]:
        return "Stalemate"



if f1[0] not in letters or f2[0] not in letters or f3[0] not in letters:
    print("Error: буква не верна")
elif f1[1] not in digits or f2[1] not in digits or f3[1] not in digits:
    print("Error: цифра не верна")
elif f1==f2 or f1==f3 or f2==f3:
    print("Error: Есть фигуры, которые стоят в одном положении")
else:
    print(func(f1,f2,f3))

