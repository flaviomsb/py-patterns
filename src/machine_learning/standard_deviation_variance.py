import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100, 20, 10000)
std = round(incomes.std(), 3)
variance = round(incomes.var(), 3)

plt.hist(incomes, 50)
plt.text(35, 500, f"std={std} \nvar={variance}")
plt.show()

