import os
from PIL import Image
import numpy as np

def load_image(image_path):
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print("Lỗi từ đọc hình ảnh: ", image_path, " ", e)
        return None

def is_image_file(file_path):
    extensions = (".jpg", ".jpeg", ".png", ".bmp")
    return file_path.lower().endswith(extensions)

def get_image_list(folder_path):
    image_list = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        filenames = os.listdir(folder_path)
        for filename in filenames:
            file_path=os.path.join(folder_path, filename)
            if  os.path.isfile(file_path) and is_image_file(file_path):
                img = load_image(file_path)
                image_list.append(img)
    return image_list