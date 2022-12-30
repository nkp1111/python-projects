from PIL import Image
import numpy as np

top_colors = []
top_colors_num = 10

img = Image.open("images/cat-wall.jpg")
colors = np.array(img)
print(colors.shape)
colors = colors.reshape((749 * 1200, 3))
total_colors = colors.size

values, counts = np.unique(colors, return_counts=True, axis=0)

for i in range(top_colors_num):
    val = np.argmax(counts)
    top_colors.append((counts[val] / total_colors, values[val]))
    counts = np.delete(counts,val)

print(top_colors)
