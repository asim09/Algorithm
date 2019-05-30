# if i and i+1 is sme them remove both from a string


def rec(a):
    i, l = 0, len(a)
    while i < l - 1:
        if a[i] == a[i + 1]:
            return rec(a[:i] +  a[i + 2:])
        i += 1

    return a


if __name__ == '__main__':
    x = 'AABCCDE'
    print __name__

    print rec(x)

