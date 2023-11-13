# Tuple to dict

# Method-1
t = ((1, 'a'),(2, 'b'))
l = dict(map(reversed, t))

# Method-2
t = ((1, 'a'),(2, 'b'))
l = {y:x for x, y in t}



# Method-3
t = ((1, 'a'),(2, 'b'))
l = dict((y, x) for x, y in t)
