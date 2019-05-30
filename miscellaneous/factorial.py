def fac(n):
    if n ==1:
        return 1
    print(n, (n-1))
    return n * fac(n - 1)


print(fac(5))


# method-2

def factorial(number):
    return 1 if number == 1 else factorial(number-1) * number


print(factorial(5))
