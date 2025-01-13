import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

pageSpeeds = np.random.normal(5.0, 2.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 1, 1000)) * 2.4

slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)

def predict(x):
    return slope * x + intercept

fit_line = predict(pageSpeeds)

print(f"R = {r_value} \nStd. Error = {std_err}")

plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fit_line, c="r")
plt.xlabel('Page Loading Time')
plt.ylabel('Amount Purchased')
plt.show()
