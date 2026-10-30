
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

folder = Path(__file__).parent


data = pd.read_csv(folder / "tencent_games_practice.csv")

# print(data.head())

# x_value = [1,2,3]
# y_value =[9,5,6]

# plt.plot(x_value,y_value)
# plt.show()
# print(data['Genre'].unique())
cat_cout = data['Genre'].value_counts()
# print(cat_cout)

x_bar = cat_cout.index
y_bar = cat_cout.values
plt.bar(x_bar , y_bar , color = 'red')

# plt.figure(figsize=(12,8))
plt.xticks(rotation = 90 , fontsize = 10,color='orange')

plt.xlabel('Genre' , fontsize = 14 , color = 'red')
plt.ylabel('Count' , fontsize = 12 , color = 'pink')
plt.title('Total Count' , fontsize = 14 , color = 'yellow')
plt.show()
