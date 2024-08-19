import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

tips = sns.load_dataset("tips")


def sex_to_bit(sex: str) -> int:
    return {"Female": 0, "Male": 1}[sex]


def day_to_number(day: str) -> int:
    days_dct = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}
    return days_dct.get(day)


tips["sex"] = tips["sex"].apply(sex_to_bit)
tips["smoker"] = tips["smoker"].apply(lambda x: 0 if x == "No" else 1)
tips["time"] = tips["time"].apply(lambda x: 0 if x == "Dinner" else 1)
tips["day"] = tips["day"].apply(day_to_number)

correlation_mtx = tips.corr()
mask = np.triu(np.ones_like(correlation_mtx, dtype=bool))
print(correlation_mtx)

sns.heatmap(correlation_mtx, mask=mask, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
