from functools import wraps


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print 'Inside decorator. Calling decorated function'
        return f(*args, **kwds)
    return wrapper


@my_decorator
def example():
    """Docstring"""
    print 'Inside example function'


example()
