x = 10

# convert to float
x = float(x)

print(f"{x} as int then converted into a float {x}")

x = "120"
y = 5

print(f"x = '{x}' and y = {y} then int(x) / y = {int(x) / y}")

epsilon = 1e-3

print(f"converting float into string {epsilon} = {str(epsilon)}")

print(f"convert list into tuple {tuple({'a', 'b', 'c'})}")

print(f"convert list into dict {dict(zip({'a', 'b', 'c'}, {1, 2, 3}))}")
