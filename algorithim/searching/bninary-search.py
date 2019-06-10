# Method -1

def Binary_search(arr, start_index, last_index, element):
    while start_index <= last_index:
        mid = (int)(start_index + last_index) // 2

        if element > arr[mid]:
            start_index = mid + 1
        elif element < arr[mid]:
            last_index = mid - 1
        elif element == arr[mid]:
            return mid
    return -1


arr = [2, 3, 4, 10, 40,45,80]
element = 40
start_index = 0
last_index = len(arr) - 1
found = Binary_search(arr, start_index, last_index, element)
if found == -1:
    print("element not present in array")

else:
    print("element is present at index " + str(found))



# Method -1 Recusrion


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
