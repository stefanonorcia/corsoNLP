import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("electricity.csv",
                 header=52608,
                 parse_dates=True,
                 index_col=0)
df.plot()

plt.grid()
plt.show()
