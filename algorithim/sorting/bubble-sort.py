# Bubble sort with complexity n:
sample_list = [8, 10, 5, 3, 7, 4, 6, 1, 9]

list_length = len(sample_list)

for i in range(list_length):
    swapped = False
    for j in range(list_length - i - 1):
        if sample_list[j] > sample_list[j + 1]:
            sample_list[j], sample_list[j + 1] = sample_list[j + 1], sample_list[j]
            swapped = True
        if swapped == False:
            break
    print(sample_list)


# sort the list of tuple order by second element:

arr = [(2, 5), (1, 2), (4, 4), (2, 3)]

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)