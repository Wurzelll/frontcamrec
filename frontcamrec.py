import cv2

def kayit_yap(video_kayit_adi="kayit.mp4"):
    # VideoCapture objesini oluşturun
    cap = cv2.VideoCapture(0)

    # Video codec ve VideoWriter objesini ayarlayın
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_kayit_adi, fourcc, 20.0, (640, 480))

    while True:
        # Kameradan bir kare okuyun
        ret, frame = cap.read()

        # Eğer kare okunamazsa döngüyü sonlandırın
        if not ret:
            print("Hata: Kare okunamadı.")
            break

        # Kaydedilen videoya kareyi yazın
        out.write(frame)

        # Görüntüyü ekranda gösterin
        cv2.imshow("Kayıt", frame)

        # Klavyeden 'q' tuşuna basıldığında döngüyü sonlandırın
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kullanılan kaynakları serbest bırakın
    cap.release()
    out.release()

    # Pencereleri kapatın
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Kaydı başlatın
    kayit_yap()
