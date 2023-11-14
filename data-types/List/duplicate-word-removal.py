list = ["geeks", "for", "geeks"]


def removal(list, n,word,empty_list=[]):
    count = 0
    for elem in range(len(list)):
        print(elem)

        if list[elem] == word:
            count = count+1
            if count == n:
                del(list[elem])
    print(list)
    return list

removal(list, 2, 'geeks')
#
# l = []


