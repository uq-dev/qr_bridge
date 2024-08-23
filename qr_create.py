import pyperclip
import qrcode
from PIL import Image

# クリップボードからテキストを取得
clipboard_text = pyperclip.paste()

# QRコードを生成
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(clipboard_text)
qr.make(fit=True)

# QRコードを画像として表示
img = qr.make_image(fill='black', back_color='white')
img.show()