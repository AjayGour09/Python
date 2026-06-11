import numpy as np

prices = np.array([90,780,80])
discount = 10

final_Price = prices-(prices*discount/100)
print(final_Price)