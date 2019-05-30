
def binary_search(sample_array, number, start, end):
    if start < end:
        mid = (end+start)//2
        if sample_array[mid] < number:
            return binary_search(sample_array, number, mid + 1, end)
        elif sample_array[mid] > number:
            return binary_search(sample_array, number, start, mid)
        else:
            return mid
    else:
        return -1


sample_array = [2, 3, 4, 10, 40]
number = 10
print(binary_search(sample_array, number, 0, len(sample_array)-1 ))
