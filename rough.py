
def Binary_search(arr, start_index, last_index, element):
    i = 0
    while start_index <= last_index:
        print('-----iter----'+str(i))
        mid = (int)(start_index + last_index) // 2

        print('------start_index-----', start_index)
        print('------last_index------', last_index)
        print('------mid-----', mid)
        if element > arr[mid]:
            start_index = mid + 1
        elif element < arr[mid]:
            last_index = mid - 1
        elif element == arr[mid]:
            return mid
        i = i + 1
        print('-----iter----' + str(i))
        print()
        print()
        print()
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





