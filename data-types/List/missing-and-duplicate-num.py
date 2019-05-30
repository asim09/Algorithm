# Find missing and duplicate element

# method-1
sample_list = [1,2,3,4,5,6,7,8,8,9,10,12]
sequence = sample_list[0]
iterator = 0
while iterator < len(sample_list):
    if sample_list[iterator] == sequence:
        iterator += 1
        sequence += 1
    elif sample_list[iterator] < sequence:
        print(sample_list[iterator])
        iterator += 1
    else:
        print(sequence)
        sequence += 1



# method-2
sample_list = [1,2,3,4,5,6,7,8,8,9,10,12]
iterator = sample_list[0]
missing_list = []
duplicate_list = []


for num in sample_list:

    if iterator < num:
        missing_list.append(iterator)
        iterator += 2

    elif iterator > num:
        duplicate_list.append(num)

    elif iterator == num:
        iterator += 1

print(missing_list, duplicate_list)

