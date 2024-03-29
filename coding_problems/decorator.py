import time
import functools

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        # func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.clock()    # 1
        # print start_time
        value = func(*args, **kwargs)
        end_time = time.clock()      # 2
        run_time = end_time - start_time    # 3
        # print run_time
        # print("Finished {func.__name__!r} in {run_time:.4f} secs")
        # print 'finished in ' + str(run_time) + ' sec'
        return value
    return wrapper_timer



# Decorator function taking the name and decorate with ? in the begining and # at the end

input = 'asim'
output = '?asim#'


def decorate_name(fun):
    def inner(user_input):
        s = '?' + user_input + '#'
        return fun(s)
    return inner


@decorate_name
def get_input(user_name):
    return user_name

print(get_input(input))


'''***************************************************************************'''
array = ['a', 'b', 'c']


def decorator(func):
    def newValueOf(pos):
        if pos >= len(array):
            print("Oops! Array index is out of range")
            return
        func(pos)

    return newValueOf

@decorator
def array1(index):
    print(array[index])
array1(4)

'''***************************************************************************'''

