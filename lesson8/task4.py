from functools import wraps


def val_checker(decorate_func):
    def decorate_wrapper(func):
        @wraps(func)
        def wrapper(x):
            if decorate_func(x):
                return func(x)
            else:
                raise ValueError(f'wrong val {x}')

        return wrapper

    return decorate_wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """func calc_cube"""
    return x ** 3


print(calc_cube(5))
print(calc_cube.__name__)
print(calc_cube.__doc__)
print(calc_cube(-5))
