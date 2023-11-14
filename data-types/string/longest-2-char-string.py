# This is a problem asked by Google.
#
# Given a string, find the longest substring that contains only two unique characters.
# For example, given "abcbbbbcccbdddadacb", the longest substring that contains 2 unique
# character is "bcbbbbcccb".


def discard_previous_string(temp):
    char_buffer = []
    for i in range(len(temp)-1, -1, -1):
        if temp[i] not in char_buffer:
            char_buffer.append(temp[i])
        if len(char_buffer) > 2:
            return temp[i + 1:], temp[i]


sample_string = 'abcbbbbcccbdddadacb'

max = ''
temp = ''
char_queue = []

for i in range(len(sample_string)):
    if sample_string[i] not in temp:
        char_queue.append(sample_string[i])


    temp = temp + sample_string[i]

    if len(char_queue) > 2:
        temp, discard_element = discard_previous_string(temp)
        char_queue.remove(discard_element)
    if len(max) < len(temp):
        max = temp
