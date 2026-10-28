
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

folder = Path(__file__).parent


data = pd.read_csv(folder / "tencent_games_practice.csv")

# print(data.head())
x_value = [1,2,3]
y_value =[9,5,6]

plt.plot(x_value,y_value)
plt.show()

