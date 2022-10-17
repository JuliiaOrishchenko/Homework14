def logger(func):
    def wrapper(*args):
        a = [i for i in args]
        return f"function {func.__name__} called with {a}"
    return wrapper

@logger
def add(a, b):
    return a+b

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(add(4, 5))
print(square_all(4, 5, 6))
