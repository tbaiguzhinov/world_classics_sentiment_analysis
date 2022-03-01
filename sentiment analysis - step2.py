from PIL import Image, ImageDraw

path = "war_and_peace.csv"

with open(path, "r", encoding="utf-8") as file:
    data = file.read().split("\n")

def color_based_on_score(score):
    if score < 0:
        r, g, b = 148, 3, 6 # Red - negative
        a = - 283.333*score
    else:
        r, g, b = 0, 113, 51 # Green - positive
        a = 283.333*score
    return r, g, b, int(a)


def create_image(width, height, dots):
    item = 0
    image = Image.new("RGBA", (height*2, width*2), (0,0,0, 0))    
    draw = ImageDraw.Draw(image)
    for y in range(0, width*2+1, 2):
        if item >= len(dots):
            break
        for x in range(0, height*2+1, 2):
            if item >= len(dots):
                break
            color = dots[item]
            shape = [x,y, x+1,y+1]
            draw.ellipse(shape, fill=color, outline=color)
            item += 1
    image.save(f"{width}X{height}.png")

dots = []
for line in data:
    if len(line.split(",")) > 2:
        r,g,b,a = color_based_on_score(float(line.split(",")[-2]))
        dot = (r,g,b,a)
        dots.append(dot)

create_image(132, 90, dots)
        