import qrcode
import sys
from PIL import Image


ssid = 'test'
password = 'test'
security = 'WPA2'
filename = 'qr.png'


def main(ssid: str, password: str, security: str, filename: str) -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=20,
        border=5,
    )
    qr.add_data(f'WIFI:T:{security};S:{ssid};P:{password};;')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    png_image = Image.open("qr_code.png")
    png_image.save("qr_code.svg", "SVG")

    print("QR code exported as SVG.")



if __name__ == '__main__':
    arguments = sys.argv

    main(ssid, password, security, filename)

