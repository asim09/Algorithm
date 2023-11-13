import string


def findLongestSubstring(string):
    n = len(string)
    st = 0
    maxlen = 0
    start = 0
    pos = {}
    pos[string[0]] = 0

    for i in range(1, n):
        if string[i] not in pos:

            pos[string[i]] = i
            # print(f'={pos}=={[string[i]]}===={i}')
            # print()
        else:
            # print(f'={pos}=={[string[i]]}===={i}')
            if pos[string[i]] >= st:
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st
                st = pos[string[i]] + 1
            # print(f'==={pos}')
            # print(f'==={pos[string[i]]}==={i}')
            pos[string[i]] = i
            # print(f'={pos}=={[string[i]]}===={i}')
    # if maxlen < i - st:
    #     print('==================================')
    #     maxlen = i - st
    #     start = st
    # print(start,start + maxlen)
    return string[start: start + maxlen]


def solve(str: str) -> int:
    if len(str) == 0:
        return 0
    maxans = -1
    for i in range(len(str)):
        set = {}
        for j in range(i, len(str)):
            print(f"i-->{i}, j--->{j}, set----{set},str[j]---->{str[j]},  maxans---- {maxans}")
            if str[j] in set:
                print()
                maxans = max(maxans, j - i)
                break
            set[str[j]] = 1
        print()
    return maxans


def findLongestSubstring(string: str):
    n = len(string)
    st = 0
    maxlen = 0
    start = 0
    pos = {}
    pos[string[0]] = 0

    for i in range(1, n):
        if string[i] not in pos:
            pos[string[i]] = i
        else:
            if pos[string[i]] >= st:
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st
                st = pos[string[i]] + 1
            pos[string[i]] = i
    print(start, start + maxlen)
    return string[start: start + maxlen]

# find subarray with given sum:\





if __name__ == "__main__":
    string1 = "GEEKFORGEEKS"
    string2 = "abcaabcdba"
    # print(findLongestSubstring(string2))
    # print(solve(string2))
    # print(solve(string1))
    print(subarray_of_given_sum(array=[1, 4, 0, 0, 3, 10, 5], sum=7))