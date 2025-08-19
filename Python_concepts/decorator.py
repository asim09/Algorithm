"""
1. when we pass arbitrary no of arguments in original func.
2. we do not pass argument in decorator from original func.
functools keeps the metadata of original function which important to keep track during-
logging,
Debugging
Inspect
Unittesting
"""

import time
from functools import wraps


def timer(func):
    @wraps(func)  # Use functools.wraps to preserve metadata of the original function
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.2f} seconds")
        return result

    return wrapper


@timer
def slow_function(seconds):
    """This function simulates a delay by sleeping for a given number of seconds."""
    time.sleep(seconds)
    print(f"Function slept for {seconds} seconds")


# Call the function
slow_function(3)

# Verify metadata preservation
print(slow_function.__name__)  # Output: slow_function
print(slow_function.__doc__)  # Output: This function simulates a delay by sleeping for a given number of seconds.
"if we do not use functool  here then output of line 35 will be - None"
"******************************************************************************************8"

"3. Decorator with Arguments (Intermediate Level)"
"decorator to authenticate user"

import functools


def authenticate(get_user_role):
    def decorator(func):
        @functools.wraps(func)  # This will preserve the metadata of 'func'
        def wrapper(*args, **kwargs):
            # Dynamically get the user role
            user_role = get_user_role()
            if user_role != "admin":
                print("Access denied: You are not an admin!")
                return None
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Simulating a function to get user role dynamically
def get_current_user_role():
    # For simplicity, return a hardcoded role
    # Replace this with logic to fetch the actual user role (e.g., from a session)
    return "guest"  # Change this to "admin" to grant access


class App:
    @authenticate(get_current_user_role)
    def admin_dashboard(self):
        print("Accessing admin dashboard")

    @authenticate(get_current_user_role)
    def guest_page(self):
        print("Accessing guest page")


app = App()
app.admin_dashboard()  # Output: Access denied: You are not an admin!
app.guest_page()  # Output: Access denied: You are not an admin!
"******************************************************************************************"
"3. Decorator with Arguments (Intermediate Level)"
"Logging"

import functools
import logging

# Setting up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def authenticate(get_user_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Dynamically get the user role
            user_role = get_user_role()
            if user_role != "admin":
                # Log the access denial event
                logging.warning(f"Access denied: User with role '{user_role}' tried to access {func.__name__}.")
                print("Access denied: You are not an admin!")
                return None
            # Log the successful function access
            logging.info(f"User with role '{user_role}' accessed {func.__name__}.")
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Simulating a function to get user role dynamically
def get_current_user_role():
    # For simplicity, return a hardcoded role
    # Replace this with logic to fetch the actual user role (e.g., from a session)
    return "guest"  # Change this to "admin" to grant access


class App:
    @authenticate(get_current_user_role)
    def admin_dashboard(self):
        print("Accessing admin dashboard")

    @authenticate(get_current_user_role)
    def guest_page(self):
        print("Accessing guest page")


app = App()
app.admin_dashboard()  # Logs a warning and prints "Access denied"
app.guest_page()  # Logs a warning and prints "Access denied"

"******************************************************************************************"

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
        start_time = time.clock()  # 1
        # print start_time
        value = func(*args, **kwargs)
        end_time = time.clock()  # 2
        run_time = end_time - start_time  # 3
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


def greet_decorator(greeting):
    def decorator(func):
        def wrapper(name):
            print(f"{greeting}, {name}!")
            func(name)

        return wrapper

    return decorator


@greet_decorator("Welcome")
def say_name(name):
    print(f"My name is {name}.")


say_name("Asim")
