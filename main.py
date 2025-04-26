import numpy as np
import cv2


def zad1():
    image = cv2.imread("opencv.png")
    image = cv2.resize(image, (0, 0), fx=0.3, fy=0.3)
    (B, G, R) = cv2.split(image)
    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    cv2.imwrite("red_channel.png", R)
    cv2.imwrite("green_channel.png", G)
    cv2.imwrite("blue_channel.png", B)


def zad2():
    image = cv2.imread("flowers.jpeg")
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    (B, G, R) = cv2.split(image)

    cv2.imshow("Original", image)
    cv2.imshow("Blue Channel", B)
    cv2.imshow("Green Channel", G)
    cv2.imshow("Red Channel", R)


def zad3():
    image = cv2.imread("flowers.jpeg")
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    (B, G, R) = cv2.split(image)
    swapped = cv2.merge([R, B, G])
    cv2.imshow("Original", image)
    cv2.imshow("Changed", swapped)
    G_zero = np.zeros_like(G)
    no_green = cv2.merge([B, G_zero, R])
    cv2.imshow("Without green", no_green)


def zad4():
    image = cv2.imread("flowers.jpeg")
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    (B, G, R) = cv2.split(image)
    R_boosted = cv2.add(R, 75)
    image_boosted = cv2.merge([B, G, R_boosted])
    cv2.imshow("Original", image)
    cv2.imshow("Boosted Red", image_boosted)


def zad5():
    image = cv2.imread("flowers.jpeg")
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([10, 60, 60])
    upper_yellow = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    (B, G, R) = cv2.split(image)
    R_boosted = cv2.add(R, 120, mask=mask)
    modified = cv2.merge([B, G, R_boosted])

    cv2.imshow("Original", image)
    cv2.imshow("Yellow Mask", mask)
    cv2.imshow("Boosted Red", modified)


def zad6():
    image = cv2.imread("opencv.png")
    image = cv2.resize(image, (0, 0), fx=0.3, fy=0.3)
    (B, G, R) = cv2.split(image)

    swapped = cv2.merge([R, G, B])
    cv2.imshow("B Changed with R", swapped)

    G_zero = np.zeros_like(G)
    no_green = cv2.merge([B, G_zero, R])
    cv2.imshow("Without Green", no_green)


# zad1()
# zad2()
# zad3()
# zad4()
# zad5()
zad6()
cv2.waitKey(0)
cv2.destroyAllWindows()