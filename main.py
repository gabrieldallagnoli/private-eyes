import cv2
import subprocess
import time

url = 'http://192.168.100.189:8080/video'
cap = cv2.VideoCapture(url)

ret, frame1 = cap.read()
if not ret:
    print("Erro ao capturar o primeiro frame")
    exit(1)

gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

player_proc = None

try:
    while True:
        ret, frame2 = cap.read()
        if not ret:
            print("Falha ao capturar frame")
            break

        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

        delta = cv2.absdiff(gray1, gray2)
        thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        motion = any(cv2.contourArea(c) > 5000 for c in contours)

        if motion:
            subprocess.run([
                "notify-send",
                "Tem alguém na porta! 🐒🚪"
            ])
            if player_proc is None or player_proc.poll() is not None:
                player_proc = subprocess.Popen([
                    'mpv', '--no-terminal', '--loop',
                    '/home/gab/GitHub/pv-eyes/track.mp3'
                ])
        else:
            if player_proc is not None:
                player_proc.terminate()
                player_proc = None

        gray1 = gray2

        if cv2.waitKey(1) == 27:  # ESC
            break

        time.sleep(0.1)

finally:
    if player_proc is not None:
        player_proc.terminate()
    cap.release()
    cv2.destroyAllWindows()