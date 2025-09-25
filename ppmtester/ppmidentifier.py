from PIL import Image

def get_ppm_data_with_pillow(filename):
    img = Image.open(filename)
    pixels = list(img.getdata())
    return pixels


def compare_ppm(name, tolerable: int):
    source_data = get_ppm_data_with_pillow("testers/" + name + ".ppm")
    new_data = get_ppm_data_with_pillow("new/" + name + ".ppm")
    for i in range(0,len(source_data)):
        if (abs(source_data[i][0] - new_data[i][0]) >= tolerable)\
                or (abs(source_data[i][1] - new_data[i][1]) >= tolerable)\
                or (abs(source_data[i][2] - new_data[i][2]) >= tolerable):
            print("error at ", i)



compare_ppm("demosaicked", 10)