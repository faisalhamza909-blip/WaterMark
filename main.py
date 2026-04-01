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

def watermark_logo(input_path, logo_path):
    base = Image.open(input_path).convert("RGBA")
    logo = Image.open(logo_path).convert("RGBA")


    logo = logo.resize((100, 100))

    width, height = base.size
    logo_width, logo_height = logo.size

    x = width - logo_width - 10
    y = height - logo_height - 10

    # paste logo
    base.paste(logo, (x, y), logo)

    base.save("output_logo.png")
    base.show()

# text = input("Enter the text\n")
# watermark_text("random_img.jpg", text)
watermark_logo("random_img.jpg","logo.png")