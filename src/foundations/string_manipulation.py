single_quote = "hello"
double_quote = "world"

# length
single_quote_len = len(single_quote)

# accessing a char in a string
single_quote[1]  # e

# string slicing
single_quote[0:2]  # he
single_quote[:2]  # he
single_quote[2:]  # llo
single_quote[-3:]  # llo

# concatenation
hw = single_quote + " " + double_quote  # hello world

# repetition
single_quote * 3  # hello hello hello

# Some string methods
single_quote.lower()  # hello
single_quote.upper()  # HELLO
single_quote.capitalize()  # Hello
hw.split(" ")  # ['hello', 'world']
" ".join(["hello", "world"])  # hello world

# formatting

# old style
print("My name is %s and I am %d years old" % ("Martha", 23))
# str.format
print("My name is {} and I am {} years old".format("Nathan", 35))
# f strings
name = "Joe"
age = 30
print(f"My name is {name}and I am {age} years old")

# raw strings
raw_string = r"C:\Users\my_dir"
print(raw_string)
