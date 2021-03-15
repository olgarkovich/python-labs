from functools import wraps


def cached(logged=False):

    def decorator(func):
        if logged:
            print("--Initializing cache for", func.__name__)
        cache = {}

        @wraps(func)
        def function_decorator(*args, **kwargs):
            if logged:
                print("--Called function", func.__name__)
            key = args, frozenset(kwargs.items())
            result = None
            if key in cache:
                if logged:
                    print("--Cache hit for", func.__name__, key)
                    result = cache[key]
            elif logged:
                print("--Cache miss for", func.__name__, key)
            if result is None:
                result = func(*args, **kwargs)
            cache[key] = result
            return result

        return function_decorator

    return decorator


@cached(True)
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# print("Testing - F(1) = {}".format(fib(1)))
# print("Testing - F(2) = {}".format(fib(2)))
#print("Testing - F(3) = {}".format(fib(3)))
#print("Testing - F(4) = {}".format(fib(4)))
# print("Testing - F(5) = {}".format(fib(5)))
# print("Testing - F(6) = {}".format(fib(6)))
