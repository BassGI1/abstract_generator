from cv2 import resize as re, INTER_AREA, imshow, waitKey
import numpy as np
from random import randint as rand

def genImage():
    def resize(img, factor):
        width = int(img.shape[1]*factor)
        height = int(img.shape[0]*factor)
        dimensions = (width, height)
        return re(img, dimensions, interpolation=INTER_AREA)

    # def createOutline(img, thickness):
    #     col = [[0, 0, 0], [255, 255, 255]][rand(0, 1)]
    #     cannied = dilate(Canny(img, 50, 50), (3, 3), iterations=thickness)
    #     for x in range(0, len(img)):
    #         for y in range(0, len(img[x])):
    #             if cannied[x][y]:
    #                 img[x][y] = col
    #     return img

    def generateColours(cols):
        c = []
        for _ in range(1, rand(1, cols) + 1):
            c.append([rand(0, 255), rand(0, 255), rand(0, 255)])
        return c

    rules = {
        "blockSize": {
            "x-small": [500, 1],
            "small": [320, 1.5625],
            "medium": [200, 2.5],
            "large": [100, 5],
            "x-large": [20, 25]
        },
        "colours": range(1, 11)
    }

    size = input("What size would you like the segments to be? (x-small, small, medium, large, x-large) \n")
    while size.lower() not in rules["blockSize"]:
        size = input("Invalid string. Please type another value. (x-small, small, medium, large, x-large) \n")
    colours = int(input("What level of abstraction would you like? (1 - 10)\n"))
    while colours not in rules["colours"]:
        colours = int(input("Invalid value. Please type another value. (1 - 10)\n"))

    image = np.zeros((rules["blockSize"][size][0], rules["blockSize"][size][0], 3), np.uint8)

    colourChoices = generateColours(colours)
    for x in range(0, len(image)):
        for y in range(0, len(image[x])):
            c = colourChoices[rand(0, len(colourChoices) - 1)]
            image[x][y] = c

    image = resize(image, rules["blockSize"][size][1])
    return image

def averageImages(im1, im2):
    for x in range(len(im1)):
        for y in range(len(im1[x])):
            r1, g1, b1 = im1[x][y]
            r2, g2, b2 = im2[x][y]
            im1[x][y] = [(b1 + b2)/2, (g1 + g2)/2, (r1 + r2)/2]
    return im1

imshow('image', genImage())
waitKey(0)