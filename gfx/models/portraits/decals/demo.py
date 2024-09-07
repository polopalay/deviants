from PIL import Image

def move_image_with_background(input_image_path, output_image_path, x_shift, y_shift):
    # Mở ảnh
    img = Image.open(input_image_path)
    width, height = img.size

    # Lấy màu nền từ pixel đầu tiên (hoặc màu đầu tiên không trong suốt)
    background_color = img.getpixel((0, 0))

    # Tạo ảnh mới với nền là màu nền
    new_img = Image.new("RGBA", (width, height), background_color)

    # Di chuyển ảnh theo tọa độ x_shift và y_shift
    for y in range(height):
        for x in range(width):
            # Kiểm tra pixel không trong suốt
            pixel_color = img.getpixel((x, y))
            if pixel_color[3] > 0:  # Kiểm tra kênh alpha (để không di chuyển pixel trong suốt)
                new_x = (x + x_shift) % width
                new_y = (y + y_shift) % height
                new_img.putpixel((new_x, new_y), pixel_color)

    # Lưu ảnh mới
    new_img.save(output_image_path)

# Ví dụ sử dụng
move_image_with_background('brand.dds', 'brand2.dds', 0, -100)

