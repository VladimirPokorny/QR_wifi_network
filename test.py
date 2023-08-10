from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (200, 80))

draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 30)

draw.text((20, 20), "Hello World", font=font)

bbox = draw.textbbox((20, 20), "Hello World", font=font)
print(bbox)

image.show()