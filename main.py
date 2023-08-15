import qrcode
# import sys
from PIL import Image, ImageFont, ImageDraw

# 200 x 200 px
# 800 x 480 px

ssid = 'x' * 5
password = 'x' * 12
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

    font_size = 50
    description_font = ImageFont.truetype('fonts/consola.ttf', font_size)
    value_font = ImageFont.truetype('fonts/consola.ttf', font_size)

    img = Image.new('1', (height, width), color=(1))
    d = ImageDraw.Draw(img)

    while description_font.getlength('Password:') > 0.75 * width:
        font_size -= 0.25
        description_font = ImageFont.truetype('fonts/consola.ttf', font_size)
    
    while value_font.getlength(password) > 0.75 * width:
        font_size -= 0.25
        value_font = ImageFont.truetype('fonts/consola.ttf', font_size)
    

    

    d.text(xy=(100, 20), text='SSID:', fill=(0), font=description_font, anchor='mt')
    d.text(xy=(100, 50), text=ssid, fill=(0), font=value_font, anchor='mt')    

    d.text(xy=(100, 100), text='Password:', fill=(0), font=description_font, anchor='mt')
    d.text(xy=(100, 130), text=password, fill=(0), font=value_font, anchor='mt')

    # d.text((10, 30), f'SSID: {ssid}', fill=(0, 0, 0))
    # d.text((10, 50), f'Password: {password}', fill=(0, 0, 0))
    img.save('text.png')


def get_size(text: str, font) -> tuple:
    """
    Return width and height of text with given font size.

    Parameters:
        text (str): Text to measure
        font (ImageFont): Font of text

    Returns:
        tuple: width and height of text
    """
    box = font.getbbox(text)

    width = box[2] - box[0]
    height = box[3] - box[1]

    return (width, height)

generate_wifi_qr(ssid, password, security, filename)

generate_text_wifi(ssid, password)

# text_size('SSID', 10)

