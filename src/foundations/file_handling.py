import datetime
import os

# write to a file
file = open("data.txt", "w")
file.write("Data header")
file.write(f"\nToday is {datetime.datetime.now()}\n")
file.close()

# read from file
file = open("data.txt", "r")
for line in file:
    print(line)

# read file using readline
line = file.readline()
while line:
    print(line)
    line = file.readline()

# read file using readlines
lines = file.readlines()
for line in lines:
    print(line)

# delete file
os.remove("data.txt")

# using with
file = open("data.txt", "w")
file.write("id\tname")
file.write("\n291\tJohn Doe")
file.write("\n739\tSarah Smith")
file.write("\n974\tTom Jordan")
file.close()

with open("data.txt", "r") as file:
    content = file.read()
    print(content)


# delete file again
os.remove("data.txt")


# handling exception
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("file not found")
finally:
    file.close()
    print("file close")
