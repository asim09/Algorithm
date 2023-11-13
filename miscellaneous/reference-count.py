import sys
apapa = 'hello'
l = apapa
k = apapa
m = [apapa]
count = sys.getrefcount(apapa)
print(count)
del apapa
print(apapa)

count = sys.getrefcount(apapa)
print(count)
