# class Poly:
def sum(*args):
    print(args)
    s = 0
    for x in args:
        s = s+x
    return s

print(sum(2,3, 1, 1))