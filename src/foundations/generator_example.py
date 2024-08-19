def count(max: int) -> int:
    count = 1

    while count <= max:
        yield count
        count += 1


counter = count(3)
print(next(counter))
print(next(counter))
