import qrcode
import sys


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



if __name__ == '__main__':
    arguments = sys.argv

    main(ssid, password, security, filename)

