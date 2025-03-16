import argparse
import imutils
import cv2


'''
1. Obrót o 45 stopni
a. Wczytaj obraz i wykonaj obrót o 45 stopni wokół jego środka.
b. Wyświetl obraz przed i po rotacji.
'''


def task1():
    image = cv2.imread("photo.jpg")
    cv2.imshow("Original", image)

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by 45 Degrees", rotated)


'''
2. Obrót o -90 stopni
a. Wczytaj obraz i obróć go o -90 stopni wokół środka.
b. Wyświetl wynik.
'''


def task2():
    image = cv2.imread("photo.jpg")

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by -90 Degrees", rotated)


'''
3. Obrót wokół narożnika
a. Obróć obraz o 30 stopni względem lewego górnego narożnika (0,0).
b. Wyświetl wynik.
'''


def task3():
    image = cv2.imread("photo.jpg")

    (h, w) = image.shape[:2]

    M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by 30 Degrees", rotated)


'''
4. Obrót o dowolny kąt
a. Pobierz od użytkownika kąt obrotu i wykonaj rotację wokół środka obrazu.
b. Wyświetl wynik.
'''


def task4():
    image = cv2.imread("photo.jpg")

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    angle = float(input("Podaj kąt obrotu w stopniach: "))

    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated", rotated)


'''
5. Obrót o 180 stopni za pomocą imutils.rotate
a. Skorzystaj z imutils.rotate , aby obrócić obraz o 180 stopni.
b. Wyświetl wynik.
'''


def task5():
    image = cv2.imread("photo.jpg")

    rotated = imutils.rotate(image, 180)
    cv2.imshow("Rotated by 180 Degrees", rotated)


'''
6. Obrót bez przycinania ( rotate_bound )
a. Wykorzystaj imutils.rotate_bound , aby obrócić obraz o -33 stopnie i uniknąć
przycięcia.
b. Wyświetl wynik.
'''


def task6():
    image = cv2.imread("photo.jpg")

    rotated = imutils.rotate_bound(image, -33)
    cv2.imshow("Rotated by -33 Degrees", rotated)


'''
7. Porównanie warpAffine i imutils.rotate
a. Wykonaj obrót o 60 stopni dwoma sposobami: za pomocą cv2.warpAffine i
imutils.rotate .
b. Porównaj wyniki i zwróć uwagę na różnice.
'''


def task7():
    image = cv2.imread("photo.jpg")

    rotated_imutils = imutils.rotate(image, 60)
    cv2.imshow("Rotated by 60 Degrees with imutils", rotated_imutils)

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
    rotated_affine = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by 60 Degrees with warpAffine", rotated_affine)

'''
8. Obrót sekwencyjny
a. Wykonaj trzy obroty po 30 stopni wokół środka obrazu i wyświetl wynik
końcowy.
b. Sprawdź, czy wynik różni się od pojedynczego obrotu o 90 stopni.
'''


def task8():
    image = cv2.imread("photo.jpg")

    rotated_90 = imutils.rotate(image, 90)
    cv2.imshow("Rotated once by 90 Degrees", rotated_90)

    rotated_3x_30 = image

    for i in range(3):
        rotated_3x_30 = imutils.rotate(rotated_3x_30, 30)

    cv2.imshow("Rotated once by 30 Degrees 3 times", rotated_3x_30)


'''
9. Obrót i zapis obrazu
a. Obróć obraz o 75 stopni i zapisz wynik do pliku rotated_output.jpg .
'''


def task9():
    image = cv2.imread("photo.jpg")

    rotated = imutils.rotate(image, 75)
    cv2.imwrite("rotated_output.jpg", rotated)


'''
10. Obrót w pętli
a. Wykonaj pętlę, która obraca obraz co 15 stopni od 0 do 360 i wyświetla
każdą wersję na ekranie.
b. Dodaj opóźnienie cv2.waitKey(500) , aby obserwować zmiany.
'''


def task10():
    image = cv2.imread("photo.jpg")

    for i in range(0, 361, 15):
        rotated = imutils.rotate(image, i)
        cv2.imshow(f"Rotated by {i} Degrees", rotated)
        cv2.waitKey(500)


# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
# task7()
# task8()
# task9()
task10()

cv2.waitKey(0)
cv2.destroyAllWindows()
