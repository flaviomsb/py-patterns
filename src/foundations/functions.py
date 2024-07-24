def sum(n1: int, n2: int) -> int:
    """adds two numbers"""
    return n1 + n2


x = sum(2, 3)

print("sum(2, 3) is %d" % x)
print(sum.__doc__)  # prints function documentation


# global variable
def addUp(n: int) -> int:
    global x
    if x >= 5:
        x **= 2

    return x + n


print(f"addUp(2) is {addUp(2)}")


# exception handling
def div(n1, n2) -> float:
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print("cannot divide by zero")
    except TypeError:
        print("Can only divide numbers")
    else:
        return result


print(div(10, 4))
print(div(2, 0))
print(div("sjkd", 4))
