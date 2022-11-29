import cv2 as cv
import numpy as np
from random import randint as rand

def genImage():
    def resize(img, factor):
        width = int(img.shape[1]*factor)
        height = int(img.shape[0]*factor)
        dimensions = (width, height)
        return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

    def createOutline(img, thickness):
        col = [[0, 0, 0], [255, 255, 255]][rand(0, 1)]
        cannied = cv.dilate(cv.Canny(img, 50, 50), (3, 3), iterations=thickness)
        for x in range(0, len(img)):
            for y in range(0, len(img[x])):
                if cannied[x][y]:
                    img[x][y] = col
        return img

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
        "colours": range(1, 11),
        "outline": range(1, 4)
    }

    size = input("What size would you like the segments to be? (x-small, small, medium, large, x-large) \n")
    while size.lower() not in rules["blockSize"]:
        size = input("Invalid string. Please type another value. (x-small, small, medium, large, x-large) \n")
    colours = int(input("What level of abstraction would you like? (1 - 10)\n"))
    while colours not in rules["colours"]:
        colours = int(input("Invalid value. Please type another value. (1 - 10)\n"))
    outline = int(input("What level of outlining would you like? (1 - 3)\n"))
    while outline not in rules["colours"]:
        outline = int(input("Invalid value. Please type another value. (1 - 3)\n"))

    image = np.zeros((rules["blockSize"][size][0], rules["blockSize"][size][0], 3), np.uint8)

    colourChoices = generateColours(colours)
    for x in range(0, len(image)):
        for y in range(0, len(image[x])):
            c = colourChoices[rand(0, len(colourChoices) - 1)]
            image[x][y] = c

    image = resize(image, rules["blockSize"][size][1])
    return image

cv.imshow('image', genImage())
cv.waitKey(0)