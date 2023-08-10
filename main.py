import qrcode
# import sys
from PIL import Image, ImageFont, ImageDraw

# 200 x 200 px

ssid = 'x' * 32
password = 'x' * 32
security = 'WPA2'
filename = 'qr.png'


def generate_wifi_qr(ssid: str, password: str, security: str, filename: str) -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        border=1,
    )
    qr.add_data(f'WIFI:T:{security};S:{ssid};P:{password};;')

    print(len(qr.get_matrix()[0]))

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


def text_size(text: str, font_size: int) -> tuple:
    """
    Return width and height of text with given font size.

    Parameters:
        text (str): Text to measure
        font_size (int): Font size of text

    Returns:
        tuple: Width and height of text
    """
    font = ImageFont.truetype('arial', font_size)
    return font.getsize(text)


def generate_text_wifi(ssid: str, password: str) -> None:
    """
    Generate picture 200 x 200 px with text SSID and password which fits the screen.
    
    Parameters:
        ssid (str): SSID of the network
        password (str): Password of the network
    """
    height = 200
    width = 200

    font_size = 10
    font = ImageFont.truetype('fonts/consola.ttf', font_size)

    img = Image.new('RGB', (height, width), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    print(font.getsize('SSID')[0])

    d.text((10, 10), 'SSID:', fill=(0, 0, 0))
    d.text((10, 30), f'SSID: {ssid}', fill=(0, 0, 0))
    d.text((10, 50), f'Password: {password}', fill=(0, 0, 0))
    img.save('text.png')


generate_wifi_qr(ssid, password, security, filename)

generate_text_wifi(ssid, password)

text_size('SSID', 10)

