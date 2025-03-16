import imutils
import numpy as np
import cv2


'''
1. Podstawowe przesunięcie
a. Załaduj dowolny obraz i wyświetl go w oryginalnej postaci.
b. Przesuń obraz o 30 pikseli w prawo i 40 pikseli w dół za pomocą macierzy
transformacji M oraz cv2.warpAffine.
c. Wyświetl wynik.
'''


def task1():
    image = cv2.imread("photo.jpg")
    cv2.imshow("Original Image", image)

    M = np.float32([[1, 0, 30], [0, 1, 40]])
    shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Shifted Image", shifted_image)


'''
2. Przesunięcie w przeciwnym kierunku
a. Wykorzystaj ten sam obraz co wcześniej.
b. Przesuń go o 20 pikseli w lewo i 50 pikseli w górę.
c. Wyświetl wynik.
'''


def task2():
    image = cv2.imread("photo.jpg")

    M = np.float32([[1, 0, -20], [0, 1, -50]])
    shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Shifted Image", shifted_image)


'''
3. Eksperymentowanie z dużymi wartościami przesunięcia
a. Przesuń obraz o więcej niż połowę jego szerokości i wysokości.
b. Sprawdź, co dzieje się z pikselami, które wychodzą poza zakres
oryginalnego obrazu.
'''


def task3():
    image = cv2.imread("photo.jpg")

    M = np.float32([[1, 0, -250], [0, 1, -375]])
    shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Shifted Image", shifted_image)


'''
4. Wykorzystanie funkcji imutils.translate
a. Przesuń obraz o 50 pikseli w dół i 100 pikseli w prawo za pomocą
imutils.translate .
b. Porównaj wynik z przesunięciem wykonanym wcześniej przez cv2.warpAffine .
Czy zauważyłeś różnice?
'''


def task4():
    image = cv2.imread("photo.jpg")

    M = np.float32([[1, 0, -100], [0, 1, -150]])
    shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Shifted with M", shifted_image)

    shifted = imutils.translate(image, -100, -150)
    cv2.imshow("Shifted with mutils", shifted)


'''
5. Dynamiczne przesunięcie na podstawie parametrów użytkownika
a. Zmodyfikuj kod, aby użytkownik mógł podać wartości przesunięcia tx i ty
poprzez wprowadzenie ich z klawiatury (np. przy użyciu input())
b. Sprawdź, jak działa przesunięcie dla różnych wartości.
'''


def task5():
    image = cv2.imread("photo.jpg")

    tx = int(input("Podaj przesunięcie w poziomie (tx): "))
    ty = int(input("Podaj przesunięcie w pionie (ty): "))

    shifted = imutils.translate(image, tx, ty)
    cv2.imshow("Shifted image", shifted)


# task1()
# task2()
# task3()
# task4()
task5()

cv2.waitKey(0)
cv2.destroyAllWindows()
