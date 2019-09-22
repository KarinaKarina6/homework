def f(a):
    if isinstance(a,int):
        if a%3==0 and a%5==0:
            return 'Foobar'
        elif a%3==0:
            return 'Foo'
        elif a%5==0:
            return 'Bar'

print(f(15))
print(f(10))
print(f(12))