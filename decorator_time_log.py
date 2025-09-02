import functools
import time
def my_new_decorator(f):
    @functools.wraps(f)  # preserving __name__ and __doc__
    def wrapper_my_new_decorator(*args, **kwargs):
        t1=time.time()
        result = f(*args, **kwargs)
        t2=time.time()
        print(f'time taken is {t2-t1}')
        return result

    return wrapper_my_new_decorator

@my_new_decorator
def just_a_func(x):
    """
    This is the docstring of just_a_func.
    """
    print(f'I\'m just a function. x = {x}')
    for i in range(1,100000000000):
        if i==100000:
            print(i)
            break
    return x * x

result1 = just_a_func(100)

print(result1)
