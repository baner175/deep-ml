import numpy as np
def calculate_brightness(img):
    # Write your code here
    sum = 0
    if not img:
        return -1
    last_length = len(img[0])
    for row in img:
        if len(row) != last_length:
            return -1
        elif min(row) < 0 or max(row) > 255:
            return -1
        else:
            sum += np.sum(row)
            last_length = len(row)
    return sum/(len(img)*last_length)