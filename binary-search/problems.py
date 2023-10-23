from access_fun import evaluate_test_cases
import test_cases

# sample_list = [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]

'''Binary Search - Count the rotations of a given sorted list:'''


def binary_count_rotation(array):
    sample_list = array['input']['nums']
    position = 0
    lo, hi = 0, len(sample_list) - 1

    while position < len(sample_list):
        mid = (lo + hi)//2

        print(f"lo: {lo} hi: {hi} mid - {mid} sample_list[mid]: {sample_list[mid]}")

        if sample_list[mid - 1] > 0 and sample_list[mid - 1] > sample_list[mid]:
            return mid
        elif sample_list[mid] < sample_list[hi]:
            hi = mid - 1
        elif sample_list[mid] > sample_list[hi]:
            lo = mid + 1

        position += 1

    return 0


evaluate_test_cases(binary_count_rotation, test_cases.tests_binary_count_rotation)










# sample_list = [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]

'''Linear search - Count the rotations of a given sorted list:'''


def linear_count_rotation(array):
    sample_list = array['input']['nums']
    position = 0

    while position < len(sample_list):
        # print(position, sample_list[position], sample_list[position -1])
        if position > 0 and sample_list[position] < sample_list[position - 1]:
            return position
        position += 1
    return 0


# print(count_rotation(sample_list))
# evaluate_test_cases(linear_count_rotation, test_cases.tests_count_rotation)

