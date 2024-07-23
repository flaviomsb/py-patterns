fruits = ["apple", "mango", "lime"]
same_fruits = fruits
other_fruits = ["melon", "blueberry", "raspberry"]

print(
    f"fruits = {fruits}\nsame_fruits = fruits then {same_fruits}\nother_fruits = {other_fruits}"
)
print("\n")
print(f"fruits is same_fruits {fruits is same_fruits}")
print(f"fruits is other_fruits {fruits is other_fruits}")
print(f"fruits is not other_fruits {fruits is not other_fruits}")
