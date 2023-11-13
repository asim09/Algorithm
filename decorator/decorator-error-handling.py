array = ['a', 'b', 'c']


def decorator(func):
    def newValueOf(pos):
        if pos >= len(array):
            print("Oops! Array index is out of range")
            return
        func(pos)

    return newValueOf

@decorator
def array1(index):
    print(array[index])


array1(4)
