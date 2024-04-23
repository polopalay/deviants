from PIL import Image

def shift_image(image_path, shift, direction='up'):
    """
    Shifts an image up or down except for the background color.

    Args:
    - image_path: Path to the image file.
    - shift: The number of pixels to shift the image.
    - direction: 'up' to move the image up, 'down' to move it down.
    
    Returns:
    - A new PIL Image object with the modified image.
    """
    # Load the image
    img = Image.open(image_path)
    pixels = img.load()

    # Determine the background color from the first pixel
    background_color = pixels[0, 0]

    # Create a new image with the same size and mode
    new_img = Image.new(img.mode, img.size, background_color)
    new_pixels = new_img.load()

    # Calculate the range of pixels to move
    if direction == 'up':
        source_range = range(shift, img.height)
        target_range = range(0, img.height - shift)
    elif direction == 'down':
        source_range = range(img.height - shift - 1, -1, -1)
        target_range = range(img.height - 1, shift - 1, -1)

    # Copy pixels from the old image to the new one, skipping the background
    for y_src, y_dst in zip(source_range, target_range):
        for x in range(img.width):
            if pixels[x, y_src] != background_color:
                new_pixels[x, y_dst] = pixels[x, y_src]

    return new_img

# Usage example
# Assuming the image is 'input.jpg', shift the image up by 100 pixels
result_image = shift_image('./lust_brand2.dds', 55, 'up')

# Save the modified image to a new file
result_image.save('./lust_brand.png')

