import numpy as np
import cv2


def zad1():
    image = cv2.imread("person.jpg")
    cv2.imshow("Original", image)

    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.circle(mask, (700, 230), 200, 255, -1)
    masked = cv2.bitwise_and(image, image, mask=mask)

    # show the output images
    cv2.imshow("Circular Mask", mask)
    cv2.imshow("Mask Applied to Image", masked)
    cv2.waitKey(0)


def zad2():
    image = cv2.imread("person.jpg")
    cv2.imshow("Original", image)

    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mask, (580, 165), (815, 250), 255, -1)
    inverted_mask = cv2.bitwise_not(mask)

    masked = cv2.bitwise_and(image, image, mask=inverted_mask)

    cv2.imshow("Mask Applied to Image", masked)
    cv2.waitKey(0)


def zad3():
    image = cv2.imread("flowers.jpeg")
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow("Original", image)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([20, 20, 80])
    upper_yellow = np.array([30, 255, 255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("Yellow Mask", mask)
    cv2.imshow("Extracted Yellow Color", result)


# zad1()
# zad2()
zad3()
cv2.waitKey(0)
cv2.destroyAllWindows()