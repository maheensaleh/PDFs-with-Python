import inspect

def dec (f):
    def wrapper(a,*b,**c):
        f_args = inspect.getargspec(f).args
        print("args: ",f_args)
        return f(a,*b)
    return wrapper

# print(foo(*foo_args))
@dec
def foo(a,b,c):
    return "three"+a+b+c;

print(foo("1","2","3"))