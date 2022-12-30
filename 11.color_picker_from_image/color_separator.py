from PIL import Image
import numpy as np


def get_top_colors(image="images/cat-wall.jpg", number_of_colors=10):
    top_colors = []
    img = Image.open(image)
    colors = np.array(img)
    print(colors.shape)
    colors = colors.reshape((749 * 1200, 3))
    total_colors = colors.size
    values, counts = np.unique(colors, return_counts=True, axis=0)

    for i in range(number_of_colors):
        val = np.argmax(counts)
        top_colors.append((counts[val] / total_colors, values[val]))
        counts = np.delete(counts,val)

    return top_colors
