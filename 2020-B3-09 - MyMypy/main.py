from functools import wraps


def mymypy(*types):
    def decorator(f):
        @wraps(f)
        def wrapped(*args):
            for x, t in zip(args, types):
                if not isinstance(x, t):
                    raise TypeError(f"{x!r} is not of type {t.__name__!r}")

            return f(*args)
    
        return wrapped
    
    return decorator


@mymypy(int, int)
def test(a, b):
    print(a + b)


test(1, 2)
test("1", 2)