def decorator(func):
    def wrapper(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except Exception as ex:
            return ex
    return wrapper

@decorator
def f(х):
    return 5/х

print(f(5))
print(f(0))
print(f("word"))
print(f())

