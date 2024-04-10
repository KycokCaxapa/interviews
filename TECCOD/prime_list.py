from typing import List


def prime_list(mini: int, maxik: int) -> List[int]:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for divider in range(2, int(num**0.5) + 1):
            if num % divider == 0:
                return False
        return True

    return list(num for num in range(mini, maxik + 1) if is_prime(num))
    