import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2)

page_speeds = np.random.normal(3, 1, 100)
purchase_amount = np.random.normal(50, 30, 100) / page_speeds

train_x = page_speeds[:80]
test_x = page_speeds[80:]

train_y = purchase_amount[:80]
test_y = purchase_amount[80:]

def plot(x_set, y_set, title, deg = 6):
    x = np.array(x_set)
    y = np.array(y_set)

    p4 = np.poly1d(np.polyfit(x, y, deg))

    xp = np.linspace(0, 7, 100)

    axes = plt.axes()
    axes.set_xlim(0, 7)
    axes.set_ylim(0, 200)
    plt.title(title)
    plt.scatter(x, y)
    plt.plot(xp, p4(xp), c = 'r')
    plt.show()

# trainning data
plot(train_x, train_y, 'Training Data')

# test data
plot(test_x, test_y, 'Test Data')
