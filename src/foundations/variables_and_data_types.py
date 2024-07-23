# integer
x = 10

# float
y = 23.492

# complex number (wow)
complex_num = 5 + 3j

# Scientific notation
epsilon = 10e-3

# string (str)
name = "Joe Doe"

# string (multiline)
instructions = """
    In Python, you can represent scientific notation numbers using the e or E notation.
    This is commonly used for very large or very small numbers and allows you to express
    numbers as a product of a coefficient and a power of 10
"""

# list
ids = [4872, 789328, 578823]

# tuple
point = (12.3, 43.1)
# single element tuple requires trailing comma
parm = (32,)

# dictionary (dict)
user = {
    "name": "John Doe",
    "id": 23098402,
}

# Set (mutable)
products = {"laptop", "iPod", "headset"}

# Set (immutable)
final_states = frozenset({"not_started", "in_progress", "completed"})

# boolean (bool)
is_enabled = True

# None (equivalent to null in some languages)
result = None

print(
    x,
    y,
    complex_num,
    epsilon,
    name,
    instructions,
    ids,
    point,
    parm,
    user,
    products,
    final_states,
    is_enabled,
    result,
    sep="\n",
)
