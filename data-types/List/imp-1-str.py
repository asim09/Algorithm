# if i and i+1 is sme them remove both from a string

x = "AABCCDE"
def rec(a):
    i, l = 0, len(a)
    while i < l - 1:
        if a[i] == a[i + 1]:
            return rec(a[:i] +  a[i + 2:])
        i += 1

    return a

# Method -2
x = "AABCCDE"
stack = []

for char in x:
    if stack and stack[-1] == char:
        stack.pop()  # Remove the last character from the stack if it's the same as the current one
    else:
        stack.append(char)
    print(stack)

