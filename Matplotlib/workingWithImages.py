import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("myimg.png")
print(plt.imshow(img))
print(plt.axis('off'))
print(plt.show())
