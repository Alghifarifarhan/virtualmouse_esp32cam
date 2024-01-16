import cv2
import numpy as np
import urllib.request
import deteksitangan as st
import autopy
import pyautogui
import time

lebar_gambar, tinggi_gambar = 640, 480
luas_persegi = 70
kehalusan = 7

waktu_sebelumnya = 0
previouslocationX, previouslocationY = 0, 0
currentlocationX, currentlocationY = 0, 0

# ubah esp32 url sesuai dengan ip dari serial monitor arduino
esp32_camera_url = "http://192.168.193.64/cam-mid.jpg"

deteksi_tangan = st.handDetector(maxHands=1)
lebarLayar, tinggiLayar = autopy.screen.size()

while True:
    # Fetch the image from the ESP32 camera URL
    img_resp = urllib.request.urlopen(esp32_camera_url)
    img_arr = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    gambar = cv2.imdecode(img_arr, -1)

    gambar = deteksi_tangan.findHands(gambar)
    landmark_list, bunding_box = deteksi_tangan.findPosition(gambar)

    if len(landmark_list) != 0:
        x1, y1 = landmark_list[4][1:]
        x2, y2 = landmark_list[8][1:]
        x3, y3 = landmark_list[12][1:]
        x4, y4 = landmark_list[16][1:]
        x5, y5 = landmark_list[20][1:]

        jari = deteksi_tangan.fingersUp()
        cv2.rectangle(gambar, (luas_persegi, luas_persegi), (lebar_gambar - luas_persegi, tinggi_gambar - luas_persegi),
                      (255, 0, 255), 2)
        if jari[1] == 1 and jari[2] == 1:
            kordinat_x = np.interp(
                x2, (luas_persegi, lebar_gambar-luas_persegi), (0, lebarLayar))
            kordinat_y = np.interp(
                y2, (luas_persegi, tinggi_gambar-luas_persegi), (0, tinggiLayar))

            currentlocationX = previouslocationX + \
                (kordinat_x - previouslocationX) / kehalusan
            currentlocationY = previouslocationY + \
                (kordinat_y - previouslocationY) / kehalusan

            autopy.mouse.move(lebarLayar - currentlocationX, currentlocationY)
            cv2.circle(gambar, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            previouslocationX, previouslocationY = currentlocationX, currentlocationY

            jarak, gambar, lineInfo = deteksi_tangan.findDistance(
                8, 12, gambar)

            if jari[0] == 1 and jari[1] == 1 and jari[2] == 1 and jari[3] == 1 and jari[4] == 1:
                cv2.circle(
                    gambar, (lineInfo[4], lineInfo[5]), 15, (0, 0, 255), cv2.FILLED)
                autopy.mouse.toggle(None, down=True)
        
        if jari[1] == 1 and jari[2] == 0:
    
            jarak, gambar, lineInfo = deteksi_tangan.findDistance(
                8, 12, gambar)

            if jarak > 40:
                cv2.circle(
                    gambar, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click(button="RIGHT")

        if jari[1] == 0 and jari[2] == 1:

            jarak, gambar, lineInfo = deteksi_tangan.findDistance(
                8, 12, gambar)

            if jarak > 40:
                cv2.circle(
                    gambar, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click(button="LEFT")

    waktu_saat_ini = time.time()
    fps = 1 / (waktu_saat_ini - waktu_sebelumnya)
    waktu_sebelumnya = waktu_saat_ini
    cv2.putText(gambar, str(int(fps)), (500, 58),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 8, 8), 3)

    cv2.imshow("Image", gambar)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
