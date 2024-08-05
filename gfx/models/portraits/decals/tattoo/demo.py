from PIL import Image
import numpy as np

def shift_image_dds(image_path, x, y, output_path):
    # Mở ảnh
    image = Image.open(image_path)
    image = image.convert("RGBA")  # Đảm bảo ảnh có kênh alpha

    # Lấy kích thước ảnh
    width, height = image.size

    # Chuyển ảnh thành mảng numpy
    img_array = np.array(image)

    # Lấy pixel đầu tiên làm background
    background_pixel = img_array[0, 0]

    # Tạo mảng mới cho ảnh dịch chuyển
    shifted_img_array = np.zeros_like(img_array)
    shifted_img_array[:, :] = background_pixel  # Điền background bằng pixel đầu tiên

    # Tính toán vị trí mới cho các pixel
    for i in range(height):
        for j in range(width):
            new_i = (i + y) % height
            new_j = (j + x) % width
            shifted_img_array[new_i, new_j] = img_array[i, j]

    # Chuyển mảng numpy trở lại thành ảnh
    shifted_image = Image.fromarray(shifted_img_array)

    # Lưu ảnh mới
    shifted_image.save(output_path, format='DDS')

# Sử dụng hàm
shift_image_dds('./tattoo_02_temp.dds', 0, 160, './tattoo_02.dds')

