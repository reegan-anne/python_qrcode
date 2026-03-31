from PIL import Image, ImageDraw


def to_pil(img):
    """Convert a qrcode StyledPilImage (or any image wrapper) to a PIL Image."""
    if isinstance(img, Image.Image):
        return img
    if hasattr(img, 'get_image'):
        return img.get_image()
    return img


def style_inner_eyes(img):
    img_size = img.size[0]
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((60, 60, 90, 90), fill=255)  # top left eye
    draw.rectangle((img_size - 90, 60, img_size - 60, 90), fill=255)  # top right eye
    draw.rectangle((60, img_size - 90, 90, img_size - 60), fill=255)  # bottom left eye
    return mask


def style_outer_eyes(img):
    img_size = img.size[0]
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((40, 40, 110, 110), fill=255)  # top left eye
    draw.rectangle((img_size - 110, 40, img_size - 40, 110), fill=255)  # top right eye
    draw.rectangle((40, img_size - 110, 110, img_size - 40), fill=255)  # bottom left eye
    draw.rectangle((60, 60, 90, 90), fill=0)  # top left eye
    draw.rectangle((img_size - 90, 60, img_size - 60, 90), fill=0)  # top right eye
    draw.rectangle((60, img_size - 90, 90, img_size - 60), fill=0)  # bottom left eye
    return mask


def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im
