import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

sns.set_theme(style="darkgrid")
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="day", style="time")
plt.title(label="Tips")
plt.show()
