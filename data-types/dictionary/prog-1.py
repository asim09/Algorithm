s = 'hello world program programs word test'
l = s.split()
print(l)
d = {}
for word in l:
    if word[0] not in d:
        d[word[0]] = []
        d[word[0]].append(word)
    if word not in d[word[0]]:
        d[word[0]].append(word)
for i,j in d.items():
    print(i,": ", j)
