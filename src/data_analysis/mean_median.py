import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100, 20, 10000)
mean = round(np.mean(incomes), 3)
median = round(np.median(incomes), 3)

plt.hist(incomes, 50)
plt.text(35, 500, f"mean={mean} \nmedian={median}")
plt.show()

