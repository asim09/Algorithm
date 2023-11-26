"10. Reverse strings:"

sample_str = "geeks quiz practice code"
result = "edoc ecitcarp ziuq skeeg"


def reverse_str01(sample_str):
    rev_str = ""
    for index, char in enumerate(sample_str):
        rev_str = char + rev_str
    return rev_str


# ****************************************************************************************
"11. Reverse strings:"
"Method-1"
sample_str = "geeks quiz practice code"
result = "skeeg ziuq ecitcarp edoc"


def reverse_str02(sample_str):
    lst_a = sample_str.split(" ")
    for index, i in enumerate(lst_a):
        reversed_word = reverse_word(i)
        lst_a[index] = reversed_word
    output = " ".join(e for e in lst_a)
    return output


def reverse_word(word):
    temp_str = ""
    for char in word:
        temp_str = char + temp_str
    return temp_str


# ****************************************************************************************
sample_str = "geeks quiz practice code"
result = "edoc ecitcarp ziuq skeeg"


def reverse_str03(sample_str):
    lst_a = sample_str.split(" ")
    for index, i in enumerate(lst_a):
        lst_a[index] = i[::-1]
    output = " ".join(e for e in lst_a)
    return output


# ****************************************************************************************
string = "geeks quiz practice code"
result = "edoc ecitcarp ziuq skeeg"


def reverse_words04(string):
    stack = string.split()
    reversed_list = []
    while stack:
        reversed_list.append(stack.pop())
    fs = " ".join(e for e in reversed_list)
    return fs


# ****************************************************************************************

sample_str = "geeks quiz practice code"
result = "skeeg ziuq ecitcarp edoc"


def reverse_words05(sample_str):
    lst = sample_str.split()
    for index, word in enumerate(lst):
        lst[index] = "".join(reversed(word))
    return " ".join(lst)


# print(rev_str(sample_str) == result)

# ****************************************************************************************
sample_str = "geeks quiz practice code"
result = "skeeg ziuq ecitcarp edoc"

# sample_str1 = "Geeks"


def reverse_words06(arg1):
    print(arg1)
    char_arr = list(arg1)
    left, right = 0, len(char_arr) - 1
    while left < right:
        char_arr[left], char_arr[right] = char_arr[right], char_arr[left]
        left += 1
        right -= 1
    return "".join(e for e in char_arr)


# print(reverse_words06(sample_str1))


def rev_str(string):
    list = string.split()
    print(list)
    for index, i in enumerate(list):
        rev_word = reverse_words06(i)
        list[index] = rev_word
    return " ".join(e for e in list)
    # return None


# print(rev_str(sample_str))

# print(reverse_words05(sample_str))
"11. Reverse integer:"
integer = 12345
output = 54321


def reverse_integer01(number):
    r = int(str(integer)[::-1])
    return r


# print(reverse_integer01(number=12345))


def reverse_integer02(number):
    lst = list(str(number))
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    res = int("".join(e for e in lst))

    return res, type(res)


# print(reverse_integer02(number=12345))

"11. Reverse integer without converting it into string:"


def reverse_integer03(number):
    if isinstance(number, int) and number > 0:
        reverse_number = 0
        while number != 0:
            # print('num', number)
            last_digit = number % 10
            reverse_number = reverse_number * 10 + last_digit
            number = number // 10

        return reverse_number
    return -1


# print(reverse_integer03(number=10))
# ****************************************************************************************
'13. Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an empty string "".'
strs = ["flower", "flow", "flight"]
Output = "fl"


def longest_commom_prefix(strs):
    base = strs[0]
    for i in range(len(base)):
        print(strs[1:])
        print(i)
        for word in strs[1:]:
            print(word)
            print(
                "===i===",
                i,
                "==len(word)==",
                len(word),
                "---word[i]--",
                word[i],
                "====base[i]===",
                base[i],
            )
            print()
            if i == len(word) or word[i] != base[i]:
                return base[0:i]
    return base


print(longest_commom_prefix(strs))
