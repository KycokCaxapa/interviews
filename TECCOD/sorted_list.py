from typing import List


def sorted_list(data: List[str]) -> List[str]:
    data1 = sorted(data, key=len)
    data2 = sorted(data, key=len, reverse=True)
    return f'{data1}\n{data2}'
