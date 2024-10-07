import ctypes
import sys

total = 10

print(
    "reference counting of total variable using getrefcount is {0}".format(
        sys.getrefcount(id(total))
    )
)

new_total = total + 100

print(
    "new reference counting of total variable using getrefcount is {0}".format(
        sys.getrefcount(id(total))
    )
)


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


print(
    "reference counting of total variable using ctypes is {0}".format(
        ref_count(id(total))
    )
)
