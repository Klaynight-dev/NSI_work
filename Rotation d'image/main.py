import numpy as np
from multiprocessing import Pool

def rotate_pixel(pixel, angle):
    img = np.array([[pixel]])
    x = img.shape[1] / 2 - 0.5
    y = img.shape[0] / 2 - 0.5
    sin = np.sin(np.deg2rad(angle))
    cos = np.cos(np.deg2rad(angle))
    new_x = x * cos - y * sin
    new_y = x * sin + y * cos
    new_x += img.shape[1] / 2 - 0.5
    new_y += img.shape[0] / 2 - 0.5
    new_x = int(round(new_x))
    new_y = int(round(new_y))
    if new_x < 0 or new_x >= img.shape[1] or new_y < 0 or new_y >= img.shape[0]:
        return [0, 0, 0]
    return img[new_y][new_x]

def rotate_image(image, angle):
    pool = Pool()
    height, width, channels = image.shape
    rotated_image = np.zeros((height, width, channels), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            rotated_image[y][x] = pool.apply(rotate_pixel, args=(image[y][x], angle))
    pool.close()
    pool.join()
    return rotated_image

image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.uint8)
rotated_image = rotate_image(image, 90)
print(rotated_image)
