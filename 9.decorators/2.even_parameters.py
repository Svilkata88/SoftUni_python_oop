def even_parameters(func):
    def wrapper(*args):
        if any(not str(el).isnumeric() or el % 2 != 0 for el in args):
            return 'Please use only even numbers!'
        return func(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 2, 2))



