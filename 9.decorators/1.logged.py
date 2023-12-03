def logged(func):
    def wrapper(*args):
        return f'you called {func.__name__}({", ".join(str(a) for a in args)})\nit returned {func(*args)}'
    return wrapper

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

