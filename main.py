from PIL import Image, ImageFont, ImageDraw



def watermark_text(input_path, text):
    img = Image.open(input_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    width, height = img.size

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = width - text_width - 10
    y = height - text_height - 10

    draw.text((x, y), text, fill=(255, 255, 255, 128), font=font)

    img.save("output.png")
    img.show()


text = input("Enter the text\n")
watermark_text("random_img.jpg", text)