from PIL import Image
import os

def get_ppm_data_with_pillow(filename):
    img = Image.open(filename)
    pixels = list(img.getdata())
    return pixels


def compare_ppm(name, tolerable: int):
    source_data = get_ppm_data_with_pillow("testers/" + name)
    new_data = get_ppm_data_with_pillow("new/" + name)
    for i in range(0,len(source_data)):
        if (type(source_data[i]) == tuple):
            if (abs(source_data[i][0] - new_data[i][0]) >= tolerable) \
                    or (abs(source_data[i][1] - new_data[i][1]) >= tolerable) \
                    or (abs(source_data[i][2] - new_data[i][2]) >= tolerable):
                print("error at ", i, " for file ", name)
        elif (type(source_data[i]) == int):
            if (source_data[i] - new_data[i] >= tolerable):
                print("error at ", i, " for file ", name)

def compare_ppm_mult(tolerable: int):
    for file in os.listdir("testers"):
        compare_ppm(str(file), tolerable)

compare_ppm_mult(10)
compare_ppm("example.ppm", 10)