def add(n1: int, n2: int) -> int:
    """adds two numbers"""
    return n1 + n2


x = add(2, 3)

print("add(2, 3) is %d" % x)
print(add.__doc__)  # prints function documentation


# global variable
def exp_global(n: int) -> int:
    return x**n


print(f"exp_global(2) is {exp_global(2)}")


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


# nested functions
def calc_price(raw_price: float, tax=0.1) -> float:
    def calc_tax() -> float:
        return raw_price * tax

    return raw_price + calc_tax()


print(f"calculate price for 120.0 = {calc_price(120.0)}")


# variable-length arguments
def sumAll(*numbers):
    return sum(numbers)


print(sumAll(1, 2))

# lambda
numbers = [1, 2, 3, 4, 5]
cubic = map(lambda x: x**3, numbers)
print(list(cubic))
