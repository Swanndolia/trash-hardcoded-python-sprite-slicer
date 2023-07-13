import os
import sys
import PIL.Image
def generate_sprites(filepath, directory, filename):
    image = PIL.Image.open(filepath)
    width = image.width
    height = image.height
    for i in range(width // 64):
        column = image.crop((i * 64, 0, (i + 1) * 64, height))
        if any(pixel != 0 for pixel in column.getdata()):
            os.makedirs("/home/swanndolia/Desktop/spritesrows/sprites/" + directory, exist_ok=True)
            column.save(os.path.join("/home/swanndolia/Desktop/spritesrows/sprites/", directory, f"{filename}_{i}.png"))


def split_png(filepath, charactertype, bodypart):
    image = PIL.Image.open(filepath)
    height = image.height
    num_lines = 0
    for i in range(height // 64):
        line = image.crop((0, 64 * i, image.width, 64 * (i + 1)))
        directory = "back" if num_lines % 4 == 0 else "left" if num_lines % 4 == 1 else "front" if num_lines % 4 == 2 else "right"
        action = "_cast" if i < 4 else "_thrust" if i < 8 else "_walk" if i < 12 else "_slash" if i < 16 else "_shoot" if i < 20 else "_hurt"
        action += "_" + directory if directory != "front" else ""
        if i == (height // 64) - 1:
            directory = "front"
            action = ""
        os.makedirs("/home/swanndolia/Desktop/spritesrows/" + directory, exist_ok=True)
        line.save(os.path.join("/home/swanndolia/Desktop/spritesrows/", directory, f"{charactertype}{action}{bodypart}.png"))
        num_lines += 1
        generate_sprites(os.path.join("/home/swanndolia/Desktop/spritesrows/", directory, f"{charactertype}{action}{bodypart}.png"),directory, charactertype + action +bodypart)

def main():
    for filename in os.listdir("/home/swanndolia/Desktop/sheets"):
        if filename.endswith(".png"):
            index_second_underscore = filename.find("_", 1)
            if index_second_underscore != -1:
                split_png(os.path.join("/home/swanndolia/Desktop/sheets/", filename), filename[:index_second_underscore], filename[index_second_underscore:-4])

if __name__ == "__main__":
    main()