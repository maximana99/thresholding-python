import cv2
import matplotlib as matplotlib
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img1', img)


height, width = img.shape[0], img.shape[1]
print(img)
vector = [0] * 256
for i in range(height):
    for j in range(width):
        vector[img[i][j]] += 1

N = 2
M = 256
a = [[0 for i in range(M)] for j in range(N)]
for x in range(256):
    a[0][x], a[1][x] = x, vector[x]

print(a)
ok = False
while (not ok):
    ok = True
    for i in range(0, 255):
        if a[1][i] > a[1][i+1]:
            aux=a[1][i]
            a[1][i] = a[1][i+1]
            a[1][i+1] = aux
            aux1=a[0][i]
            a[0][i] = a[0][i+1]
            a[0][i+1] = aux1
            ok=False


print(a)


threshold = a[0][127]
print(threshold)

for i in range(height):
    for j in range(width):
        if img[i][j] < threshold:
            img[i][j] = 0
        else:
            img[i][j] = 255


cv2.imshow('img', img)


cv2.waitKey(0)
cv2.destroyAllWindows()

