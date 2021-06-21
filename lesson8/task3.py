from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for i in args:
            print(f'{func.__name__} ({i}: {type(i)}), ', end='')
        return func(*args)
    return wrapper


@type_logger
def calc_cube(*args):
    """func calc"""
    return list(map(lambda x: x ** 3, args))


print(calc_cube(5, 4))  # В конце этой строки пишется результат расчёта, хотя в задании этого нет,
# но если убрать return, то в конце пишется None, не знаю как это обойти.
print(calc_cube.__name__)
print(calc_cube.__doc__)
