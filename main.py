import os
import re
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.figure as figure
from skimage import io

def toGrayscaled(arr):
    arr = arr*[0.299, 0.587, 0.114]
    arr = arr.sum(2)
    img = Image.fromarray(arr.astype(np.uint8))
    img.save('Lena_grayscaled.png')
    return


def toThresholded(arr):
    mask = (arr >= 100).astype(int)
    arr = arr*mask
    arr = arr.astype(int)
    img = Image.fromarray(arr.astype(np.uint8))
    img.save('Lena_thresholded.png')
    return


#path = input("Enter path to image: ")
path = 'Lena.png'
if re.match(r'^.+\.png$', path) and os.path.exists(path):
    arr = np.asarray(Image.open(path))

    print('Минимальные значения: ')
    print(arr.min(0).min(0))
    print('Максимальные значения: ')
    print(arr.max(0).max(0))
    print('Средние значения: ')
    print(arr.mean(0).mean(0).astype(int))

    toGrayscaled(arr)
    arr = np.asarray(Image.open('Lena_grayscaled.png'))
    toThresholded(arr)

    image = io.imread('Lena_thresholded.png')
    ax = plt.hist(image.ravel(), bins=256)
    plt.xlabel('Интенсивность')
    plt.ylabel('Количество')
    plt.title('Гистограмма распределения яркости изображения')
    plt.show()
    Output: figure
