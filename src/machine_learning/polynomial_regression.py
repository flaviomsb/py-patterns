import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50, 10, 1000) / pageSpeeds

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 5)) # 5th degree polynomial
xp= np.linspace(0, 7, 100)

# R2
r2 = r2_score(y, p4(x))

print(f"r2_score = {r2}")

plt.scatter(x, y)
plt.plot(xp, p4(xp), c="r")
plt.xlabel('Page Loading Time')
plt.ylabel('Amount Purchased')
plt.show()
