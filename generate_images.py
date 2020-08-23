#!/usr/bin/python
import sys
from PIL import Image, ImageDraw, ImageFont

text = " ".join(sys.argv[1:])
fontSize = 40
font = ImageFont.truetype("./inconsolata.ttf", fontSize)

i1 = Image.open("1.png")
i2 = Image.open("2.png")
width, height = i1.size

text = text.split(" ")
text.insert(0, "")

if i1.size != i2.size:
    sys.exit(f"Images must have same dimemnsion ({i1.size} != {i2.size})")

# Generate texts
for i in range(1, len(text)):
    text[i] = f"{text[i - 1]}{text[i]} "
text = list(map(lambda x: x.strip(), text))
# make sure the gif loops correctly (no same frames at the start and end)
if len(text) % 2 == 1:
    text.append(text[-1])

# Calculate text position (to be centered)
while True:
    textWidth = font.getsize(text[-1], None, None, None, 0)[0]
    if textWidth > width:
        fontSize -= 1
        font = ImageFont.truetype("./inconsolata.ttf", fontSize)
    else:
        break

pos = ((width - textWidth) / 2, height - 50)


def write(img, text):
    """ writes text to give image object and returns it"""
    global font, pos
    imgd = ImageDraw.Draw(img)
    imgd.text(pos, text, font=font, fill=(0, 0, 0))
    return img


print(text)

for i in range(len(text)):
    img = None
    if i % 2 == 1:
        img = write(i1, text[i])
    else:
        img = write(i2, text[i])
    if i < 10:
        i = "0" + str(i)
    img.save(f"output{i}.png")
