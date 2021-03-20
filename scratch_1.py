from simpleimage import SimpleImage
INTENSITY_TH = 1.6

def greenscreen(main_file, back_file):
    image = SimpleImage(main_file)
    back = SimpleImage(back_file)
    for px in image:
        average = (px.red + px.green + px.blue) // 3
        if px.green >= average * INTENSITY_TH:
            x = px.x
            y = px.y
            image.set_pixel(x, y, back.get_pixel(x, y))
    return image

def main():
    original_image = SimpleImage('_IMG_20170510_132008_598.jpg')
    original_image.show()

    original_glitter = SimpleImage('glitter-wall-store-ocean-blue-glitter-wallpaper-p333-3031_image.jpg.png')
    original_glitter.show()

    orange_replaced = greenscreen('_IMG_20170510_132008_598.jpg', 'glitter-wall-store-ocean-blue-glitter-wallpaper-p333-3031_image.jpg.png')
    orange_replaced.show()

if __name__ == '__main__':
    main()