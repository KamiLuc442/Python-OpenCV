import numpy as np
import cv2


def zad1():
    triangle = np.zeros((300, 300, 1), dtype="uint8")
    pt1 = (180, 50)
    pt2 = (20, 200)
    pt3 = (280, 260)
    triangle_cnt = np.array([pt1, pt2, pt3])
    cv2.drawContours(triangle, [triangle_cnt], 0, 255, -1)
    cv2.imshow("Triangle", triangle)

    circle = np.zeros((300, 300, 1), dtype="uint8")
    cv2.circle(circle, (110, 130), 75, 255, -1)
    cv2.imshow("Circle", circle)

    bitwiseXor = cv2.bitwise_xor(triangle, circle)
    cv2.imshow("XOR", bitwiseXor)

    bitwiseAnd = cv2.bitwise_and(triangle, circle)
    cv2.imshow("AND", bitwiseAnd)

    bitwiseOr = cv2.bitwise_or(triangle, circle)
    cv2.imshow("OR", bitwiseOr)

    bitwiseXor = cv2.bitwise_xor(triangle, circle)
    cv2.imshow("XOR", bitwiseXor)

    bitwiseNot = cv2.bitwise_not(bitwiseXor)
    cv2.imshow("NOT", bitwiseNot)


def zad2():
    img1 = cv2.imread("Pic1.png")
    img2 = cv2.imread("Pic2.png")

    xor = cv2.bitwise_xor(img1, img2)

    cv2.imshow("Obraz 1", img1)
    cv2.imshow("Obraz 2", img2)
    cv2.imshow("XOR", xor)


# zad1()
zad2()
cv2.waitKey(0)
cv2.destroyAllWindows()