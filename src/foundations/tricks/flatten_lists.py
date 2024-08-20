from itertools import chain

first_list = [[1, 2], [3, 4], [5, 6]]
second_list = list(chain.from_iterable(first_list))

print(second_list)
