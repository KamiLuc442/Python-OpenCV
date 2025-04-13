import numpy as np
import cv2


def zad1(_image):
    M = np.ones(_image.shape, dtype="uint8") * 50
    added = cv2.add(_image, M)
    cv2.imshow("Zad1 cv2", added)
    cv2.waitKey(0)

    added = _image + np.uint8([50])
    cv2.imshow("Zad1 numpy", added)


def zad2(_image):
    M = np.ones(_image.shape, dtype="uint8") * 150
    added = _image + np.uint8([150])
    cv2.imshow("Zad2 numpy", added)

    added = cv2.add(_image, M)
    cv2.imshow("Zad2 cv2", added)


def zad3(_image):
    M = np.ones(_image.shape, dtype="uint8") * 80
    subbed = cv2.subtract(_image, M)
    cv2.imshow("Zad3 cv2", subbed)
    cv2.waitKey(0)

    subbed = _image - np.uint8([80])
    cv2.imshow("Zad3 numpy", subbed)


def zad4(_image):
    blue_channel = _image[:, :, 0]
    green_channel = _image[:, :, 1]
    red_channel = _image[:, :, 2]

    Mblue = np.ones(blue_channel.shape, dtype="uint8") * 10
    Mgreen = np.ones(green_channel.shape, dtype="uint8") * 20
    Mred = np.ones(red_channel.shape, dtype="uint8") * 30

    blue_plus = cv2.add(blue_channel, Mblue)
    green_minus = cv2.subtract(green_channel, Mgreen)
    red_plus = cv2.add(red_channel, Mred)

    result = cv2.merge([blue_plus, green_minus, red_plus])
    cv2.imshow("Zad 4", result)

image = cv2.imread('photo.jpg')
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# zad1(image)
# zad2(image)
# zad3(image)
zad4(image)
# zad5(image)

cv2.waitKey(0)
cv2.destroyAllWindows()
