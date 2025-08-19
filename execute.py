A = [2,4,6,7,9, 15, 16, 17, 18, 19, 20]
target = 9

def sum2_target(A):
    L = 0
    R = len(A) - 1
    while L < R:
        sum = A[L] + A[R]
        if sum == target:
            return [L, R]
        elif sum < target:
            L += 1
        else:
            R -= 1
    return -1
# print(sum2_target(A))

arr = [1, 1, 1, 0, 1, 1, 0, 1, 1]


# output = [0, 0, 1, 1, 1, 2, 2]

def sort013(array):
    array_len = len(array)
    lo, mid = 0, 0
    hi = array_len - 1
    while mid <= hi:
        if array[mid] == 0:
            array[lo], array[mid] = array[mid], array[lo]
            lo += 1
            mid += 1

        elif array[mid] == 1:
            mid += 1
    return arr