#1
def digital_root(d):
    if d//10==0:
        return d
    else:
        l=list(str(d))
        s=0
        for i in l:
             s+=int(i)
        return digital_root(s)

print(digital_root(123456))

#2

def A(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A(m-1,1)
    else:
        return A(m-1,A(m,n-1))

print(A(1,3))

#3

def rev(d):
    if d//10==0:
        return str(d)
    else:
        return str(d%10)+" "+rev(d//10)

print(rev(12345))

#4
def binar(d):
    if d==1:
        return str(1)
    else:
        return binar(d//2)+str(d%2)

print(binar(234))

#5
def f(d,k=2):
    if (k>d/2):
        return str(int(d))
    else:
        if d % k == 0:
            return str(k)+" "+f(d / k, k)
        else:
            return f(d, k + 1)


print(f(345))
