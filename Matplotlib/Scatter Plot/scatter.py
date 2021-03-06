
# -------------------------------------------------------------
# ----------------------- Scatter -----------------------------

# Scatter plots are used to observe relationship between variables and uses dots to represent the relationship
# between them. The scatter() method in the matplotlib library is used to draw a scatter plot. Scatter plots are
# widely used to represent relation among variables and how change in one affects the other.

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

plt.scatter(x, y, s=sizes, c=colors, marker='o', cmap='Greens', edgecolors='black', alpha=0.9)

bar = plt.colorbar()
bar.set_label('Color Bar')

plt.show()


