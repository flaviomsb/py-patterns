# conditional statements
x = 10

if x > 10:
    x **= 2
else:
    x -= 2

score = 95

grade = ""
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# looping constructs
for i in range(10):
    i *= 2

for i in range(20):
    if i % 2 == 0:
        continue  # skips even numbers

for i in range(15):
    if i == 10:
        break

fruits = ["apple", "mango", "lime"]
fruits_dict = {}
for index, fruit in enumerate(fruits):
    fruits_dict[index] = fruit
print(fruits_dict)

ids = [8922, 38420, 8103]
shirts = ["M", "S", "XL"]
prods = {}
for id, size in zip(ids, shirts):
    prods[id] = size
print(prods)

count = 0
while count < 5:
    count += 1
