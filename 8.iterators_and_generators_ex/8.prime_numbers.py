from typing import List


def get_primes(prime_list: List[int]):
    for num in prime_list:
        if num == 0 or num == 1 or num <0:
            continue

        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


# test code!
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
