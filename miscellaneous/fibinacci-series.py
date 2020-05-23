term = 10

n1 = 0
n2 = 1

count = 0

while count < term:
    print(n1, end=' ')
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count = count + 1


# Method -2

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return ((recur_fibo(n-1) + recur_fibo(n-2)))

for i in range(10):
    print(recur_fibo(i))
