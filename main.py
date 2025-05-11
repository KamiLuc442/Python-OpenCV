import cv2
import imutils


image = cv2.imread('kostka.png')

import cv2
import imutils


# Zad 3 a. Zmieniaj rozmiar obrazu wejściowego przed detekcją konturów. Sprawdź,
# jak zmiana rozdzielczości wpływa na liczbę i jakość wykrytych konturów.
# b. Czy zmniejszenie obrazu może poprawić detekcję?

# W moim przypadku zmiana rozmiaru na mniejszy obniża skuteczność detekcji.
def zad1(image, size):

    height, width = image.shape[:2]
    new_width = size
    scale = new_width / width
    new_height = int(height * scale)
    resized = cv2.resize(image, (new_width, new_height))

    ratio = image.shape[0] / float(resized.shape[0])

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    # thresholds = [100, 140, 200]
    thresholds = [140]

    # Zad 2 Zmieniaj tryby(parametr mode w funkcji findContours),
    # przetestuj cv2.RETR_EXTERNAL, cv2.RETR_TREE i cv2.RETR_LIST
    # i opisz różnice w komentarzu.

    # na skopiowanym obrazku z pdf różnice są nieznaczące
    # RETR_TREE i RETR_LIST wygląda mniej więcej tak samo.
    contour_modes = {
        "RETR_EXTERNAL": cv2.RETR_EXTERNAL,
        #"RETR_TREE": cv2.RETR_TREE,
        #"RETR_LIST": cv2.RETR_LIST
    }

    for thresh_val in thresholds:
        _, thresh_img = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)

        for mode_name, mode in contour_modes.items():
            image_copy = image.copy()

            brick_counter = 1
            total_width = 0
            total_height = 0
            min_width = float('inf')
            max_width = 0
            min_height = float('inf')
            max_height = 0

            cnts = cv2.findContours(thresh_img.copy(), mode, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)

            min_area = 500
            max_area = 50000

            for c in cnts:

                # Zad 6. Filtrowanie konturów po wielkości
                # a. Zaimplementuj filtrację konturów – usuwaj bardzo małe lub bardzo duże
                # kontury (np. te o powierzchni < 500 lub > 5000 pikseli).
                # b. Zastosowanie: Eliminacja szumu lub niepożądanych obiektów.
                area = cv2.contourArea(c)
                if area < min_area or area > max_area:
                    continue

                c = c.astype("float")
                c *= ratio
                c = c.astype("int")

                M = cv2.moments(c)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                else:
                    cX, cY = 0, 0

                # Zad 4. Numeryzacja kostek
                # a. Zmodyfikuj pętlę iterującą po konturach tak, by na każdej kostce (nad jej
                # środkiem) narysować numer porządkowy ( cv2.putText ).
                # b. Dodaj zapisywanie każdej wyciętej kostki do osobnego pliku kostka_01.png ,
                # kostka_02.png , itd.
                cv2.putText(image_copy, f"{brick_counter:02d}", (cX - 10, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            (0, 255, 0), 2)

                cv2.drawContours(image_copy, [c], -1, (0, 0, 255), 2)

                x, y, w, h = cv2.boundingRect(c)
                brickPic = image[y:y + h, x:x + w]
                cv2.imwrite(f"kostka_{brick_counter:02d}.png", brickPic)

                total_width += w
                total_height += h
                min_width = min(min_width, w)
                max_width = max(max_width, w)
                min_height = min(min_height, h)
                max_height = max(max_height, h)

                # Zad 5. Pomiar wymiarów kostek
                # a. Dla każdej wykrytej kostki:
                # i. Oblicz jej szerokość i wysokość w pikselach.
                # ii. Na oryginalnym obrazie narysuj prostokąt oraz opisz go wymiarami,
                # np. „40x40 px”.

                cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(image_copy, f"{w}x{h} px", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

                brick_counter += 1

            window_name = f"Contours {mode_name} (Thresh {thresh_val}, Size {size})"
            cv2.imshow(window_name, image_copy)

            # Zad 7. Liczenie i raportowanie kostek
            # a. Na końcu całego procesu wyświetl w terminalu:
            #    i. liczbę wykrytych kostek
            #    ii. ich średnią szerokość i wysokość
            #    iii. minimalny i maksymalny rozmiar
            brick_counter -= 1
            if brick_counter > 0:
                average_width = total_width / brick_counter
                average_height = total_height / brick_counter
                print(f"Krawedzie {thresh_val}")
                print(f"Wykryte kostki: {brick_counter}")
                print(f"Srednia szerokość: {average_width:.2f} px")
                print(f"Srednia wysokość: {average_height:.2f} px")
                print(f"Minimalny rozmiar: {min_width}x{min_height} px")
                print(f"Maksymalny rozmiar: {max_width}x{max_height} px")

image = cv2.imread('kostka.png')
zad1(image, size=400)

cv2.waitKey(0)
cv2.destroyAllWindows()
