import matplotlib.pyplot as plt

makes = ["GM", "Ford", "Toyota"]
sales_total = [110, 130, 230]

plt.bar(makes, sales_total)
plt.title("Bar Plot Example")
plt.xlabel("Makes")
plt.ylabel("Sales Total")
plt.show()
