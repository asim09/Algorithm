s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']


# Method - 1
l = ' '.join(map(str,s))

# Method - 2
l = ' '.join([str(e) for e in s])


# print(l)