l=[2, 'cat', 7, 2, 9, 'cat', 7, 42]
def f(a):
    k=[]
    for i in range(len(a)):
        if l[i] in k:
            pass
        else:
            k.append(l[i])
    return k

print(f(l))