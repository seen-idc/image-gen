from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from utils import get_image
from utils.masks import circle_mask

circlemask = circle_mask((256, 256))
font = ImageFont.truetype('./NunitoSans-Regular.ttf', 56)


outline_color = "#2af54f"
avatar_pos_x = 352
avatar_pos_y = 72

def generate_welcome(name, tag, avatar):
    image = Image.new('RGBA', (960, 540), (0, 0, 0, 0))
    print(name,tag)

    pfp = get_image(avatar).resize((256, 256)).convert('RGBA')

    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((0, 0 , 960, 540), 60, (3, 7, 15))
    
    image.paste(pfp, (avatar_pos_x , avatar_pos_y), circlemask)
    
    draw.ellipse((avatar_pos_x, avatar_pos_y, avatar_pos_x + 256, avatar_pos_y + 256), outline=outline_color, width=8)
    draw.textsize(f'{name}#{tag}', font)
    size = draw.textsize(f'Welcome\n{name}#{tag}', font=font)
    draw.text((960 / 2 - size[0] / 2, 72 + 256 - size[1] + 130), f'Welcome\n{name}#{tag}', font=font, align='center')

    b = BytesIO()
    image.save(b, format='png')
    b.seek(0)

    return b