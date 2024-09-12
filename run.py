sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 12, 0]
from collections import Counter

t1 = Counter(sample_list)
print(t1)

duplicates = {key for key, value in t1.items() if value > 1}
print(duplicates)
sorted_list = sorted(sample_list)
print(sorted_list)