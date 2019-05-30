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
