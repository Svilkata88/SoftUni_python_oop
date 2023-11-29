from typing import List


def possible_permutations(some_list: List) -> List:
    for i in range(len(some_list)):
        if len(some_list) <= 1:
            yield some_list
        else:
            for perm in possible_permutations(some_list[:i] + some_list[i+1:]):
                yield [some_list[i]] + perm


# test code!
[print(n) for n in possible_permutations([1, 2, 3])]
print()
[print(n) for n in possible_permutations([1])]