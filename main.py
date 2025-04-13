import numpy as np
import cv2


def zad1(_image):
    cv2.imshow("Zad1", _image[0:100, 0:100])


def zad2(_image):
    height = _image.shape[0]
    lower_half = _image[height // 2:, :]
    cv2.imshow("Zad2", lower_half)


def zad3(_image):
    width = _image.shape[1]
    right_half = _image[:, width // 2:]
    cv2.imshow("Zad3", right_half)


def zad4(_image):
    startX = int(input("Enter the startX (left): "))
    endX = int(input("Enter the endX (right): "))
    startY = int(input("Enter the startY (top): "))
    endY = int(input("Enter the endY (bottom): "))

    cv2.imshow("Zad4", _image[startY:endY, startX:endX])


def zad5(_image):
    cv2.imshow("Zad5", _image[90:525, 60:600])


def zad6(_image):
    fx1 = 60
    fx2 = 600
    fy1 = 90
    fy2 = 525
    width = fx2 - fx1
    height = fy2 - fy1
    fragment = _image[fy1:fy2, fx1:fx2]

    _image[400:400 + height, 180:180 + width] = fragment
    cv2.imshow("Zad6", _image)


def zad7(_image):
    height, width, _ = _image.shape

    cell_height = height // 3
    cell_width = width // 3

    for i in range(3):
        for j in range(3):
            fy1 = i * cell_height
            fy2 = (i + 1) * cell_height
            fx1 = j * cell_width
            fx2 = (j + 1) * cell_width

            part = image[fy1:fy2, fx1:fx2]
            cv2.imshow(f"Zad7 czesc:{i * 3 + j + 1}", part)


def zad8(_image):
    height, width, _ = image.shape
    fragx = 200
    fragy = 1000
    currentX = 0

    while True:
        key = cv2.waitKey(0)
        if key == 27:
            cv2.destroyAllWindows()
            break
        roi = image[0:fragy, 0 + currentX:fragx + currentX]
        cv2.imshow("zad8", roi)

        currentX += 10
        if (currentX + fragx >= width):
            currentX = 0


def zad9(_image):
    cropped = _image[0:500, 0:500]
    cv2.imwrite("cropped_image.jpg", cropped)
    cv2.imshow("Zad9", cropped)


image = cv2.imread('photo.jpg')
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# zad1(image)
# zad2(image)
# zad3(image)
# zad4(image)
# zad5(image)
# zad6(image)
# zad7(image)
# zad8(image)
zad9(image)
cv2.waitKey(0)
cv2.destroyAllWindows()
