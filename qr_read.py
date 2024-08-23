import cv2
import pyzbar.pyzbar as pyzbar
import pyperclip

# カメラを起動
cap = cv2.VideoCapture(0)

while True:
    # フレームをキャプチャ
    ret, frame = cap.read()

    # QRコードを検出
    decoded_objects = pyzbar.decode(frame)

    for obj in decoded_objects:
        # 読み取ったQRコードのデータをクリップボードにコピー
        qr_text = obj.data.decode('utf-8')
        pyperclip.copy(qr_text)
        print("QRコードの内容:", qr_text)

        # カメラを終了
        cap.release()
        cv2.destroyAllWindows()
        exit()

    # フレームを表示
    cv2.imshow('QRコードリーダー', frame)

    # 'q'を押すと終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラを終了
cap.release()
cv2.destroyAllWindows()