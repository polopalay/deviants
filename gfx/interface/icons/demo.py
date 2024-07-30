from PIL import Image
import os

def convert_dds_to_png(dds_file_path, png_file_path):
    try:
        with Image.open(dds_file_path) as img:
            img.save(png_file_path, 'PNG')
        print(f"File: {png_file_path}")
    except Exception as e:
        print(f"Error: {e}")

def get_all_files_in_folder(folder_path):
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return files
    except Exception as e:
        return []

original_path = './character_interactions'
new_path = './character_interactions2'

files = get_all_files_in_folder(original_path)
for file in files:
    if file.endswith('.dds'):
        dds_file_path = os.path.join(original_path, file)
        png_file_path = os.path.join(new_path, file.replace('.dds', '.png'))
        convert_dds_to_png(dds_file_path, png_file_path)


