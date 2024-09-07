from PIL import Image

def move_image_with_background(input_image_path, output_image_path, x_shift, y_shift):
    img = Image.open(input_image_path)
    width, height = img.size

    background_color = img.getpixel((0, 0))

    new_img = Image.new("RGBA", (width, height), background_color)

    for y in range(height):
        for x in range(width):
            # Kiểm tra pixel không trong suốt
            pixel_color = img.getpixel((x, y))
            if pixel_color[3] > 0:  # Kiểm tra kênh alpha (để không di chuyển pixel trong suốt)
                new_x = (x + x_shift) % width
                new_y = (y + y_shift) % height
                new_img.putpixel((new_x, new_y), pixel_color)

    new_img.save(output_image_path)

move_image_with_background('womb_2.dds', 'womb_11.png', 0, -40)
# move_image_with_background('womb_16.dds', 'womb_16.png', 0, -32)
# move_image_with_background('womb_15.dds', 'womb_15.png', 0, -32)
# n = 14
# i = 2

# for i in range(2, n):
    # move_image_with_background('womb_' + str(i) + '.dds', 'womb_' + str(i) + '.png', 0, -32)
    # i += 1
