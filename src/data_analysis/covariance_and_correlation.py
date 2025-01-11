import matplotlib.pyplot as plt 
import numpy as np

def de_mean(x):
    xmean = np.mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    std_devx = x.std()
    std_devy = y.std()
    if std_devx == 0 or std_devy == 0:
        return 0
    return covariance(x, y) / std_devx / std_devy

pageSpeeds = np.random.normal(3, 1, 1000)
purchaseAmount = np.random.normal(50, 10, 1000) / pageSpeeds

xy_correlation = correlation(pageSpeeds, purchaseAmount) 
print(f"correlation={xy_correlation}")

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()
