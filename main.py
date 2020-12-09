import os
import re
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.figure as figure
from skimage import io

def toGrayscaled(arr):
    newArr = np.empty(shape=arr.shape)
    for i in range(512):
        for j in range(512):
            list = arr[i, j]*[0.299, 0.587, 0.114]
            tmp = list[0]+list[1]+list[2]
            newArr[i, j] += [tmp, tmp, tmp]
    newArr = newArr.astype(int)
    img = Image.fromarray(newArr.astype(np.uint8))
    img.save('Lena_grayscaled.png')
    return


def toThresholded(arr):
    newArr = np.empty(shape=arr.shape)
    for i in range(512):
        for j in range(512):
            for k in range(3):
                if arr[i, j, k] < 100:
                    newArr[i, j, k] = 0
                else:
                    newArr[i, j, k] = arr[i, j, k]
    newArr = newArr.astype(int)
    img = Image.fromarray(newArr.astype(np.uint8))
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
    tmp = np.asarray([arr.size/3, arr.size/3, arr.size/3])
    print((arr.sum(0).sum(0)//tmp).astype(int))

    toGrayscaled(arr)
    arr = np.asarray(Image.open('Lena_grayscaled.png'))
    toThresholded(arr)

    image = io.imread('Lena_thresholded.png')
    ax = plt.hist(image.ravel(), bins=256)
    plt.xlabel('Интенсивность вроде')
    plt.ylabel('Какие-то штуки')
    plt.title('Гистограмма распределения яркости изображения')
    plt.show()
    Output: figure
