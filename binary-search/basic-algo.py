# Method -1
from access_fun import evaluate_test_cases
import test_cases


def locate_card(cards):
    position = 0
    lo = 0
    hi = len(cards['input']['cards']) - 1
    query = cards['input']['query']
    cards = cards['input']['cards']

    while position < len(cards):
        mid = (lo + hi) // 2
        print(f"lo: {lo} hi: {hi} mid - {mid} cards[mid]: {cards[mid]} query {query}")
        result = test_loaction(cards, query, mid)

        if result == 'found':
            return mid

        if result == 'left':
            hi = mid - 1

        if result == 'right':
            lo = mid + 1

        position += 1
    return -1


def test_loaction(cards, query, mid):
    print(query, cards[mid])
    if query == cards[mid]:

        if mid - 1 > 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'

    elif query > cards[mid]:
        return 'left'
    else:
        return 'right'


evaluate_test_cases(locate_card, test_cases.tests_locate_card)


# Method -2 Recusrion

def binary_search(sample_array, number, start, end):
    if start < end:
        mid = (end + start) // 2
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
print(binary_search(sample_array, number, 0, len(sample_array) - 1))
