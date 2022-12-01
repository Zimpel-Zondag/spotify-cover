from PIL import Image, ImageDraw, ImageFont

# const
HEIGHT = 1280
WIDTH = 1280
BORDER = 24
BORDER_BOTTOM = (HEIGHT  // 3 - BORDER)
LOGO_SIZE = 84

# inputs
RED = int(input("R: "))
GREEN = int(input("G: "))
BLUE = int(input("B: "))
TEXT = input("Text: ")
LOGO = input("Logo? (y/n): ")
FONT = ImageFont.truetype("Gotham Medium.otf", 144)

# define back- and foreground and font
background = Image.new('RGB', (HEIGHT, WIDTH), color=(RED, GREEN, BLUE))
# foreground = Image.new('RGB', (HEIGHT * 2, WIDTH * 2), color=(0, 255, 0))
foreground = Image.open("3.jpg")


# resize foreground
foreground = foreground.resize(
    (WIDTH - (2 * BORDER),
     HEIGHT - (BORDER + BORDER_BOTTOM)
     ))

# paste foreground on background
background.paste(foreground, (BORDER, BORDER))

# paste logo
if LOGO == "y":
    logo = Image.open("logo.jpg")
    logo = logo.resize((LOGO_SIZE, LOGO_SIZE))
    background.paste(logo, (BORDER + (BORDER // 2), BORDER + (BORDER // 2)))

# draw text
img = ImageDraw.Draw(background)
img.text((50, 1110), TEXT, font=FONT)

# show image
background.show()
SAVE = input("Save? (y/n) ")
if SAVE == "y":
    background.save("test.jpg")
