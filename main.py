from PIL import Image, ImageFont, ImageDraw
img = Image.open("random_img.jpg").convert("RGBA")
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((50,50),"Hamza",fill=(255,255,255,128),font= font)
img.show()
