from math import sqrt

from sys_args import print_sys_args


def calc(num: float) -> float:
    return sqrt(num)


print(calc(25))
print_sys_args()
