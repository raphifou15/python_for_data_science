import os
from PIL import Image
import numpy as np
from typing import Union


def is_str(elem) -> bool:
    """
    check if elem is of type str
    """
    if isinstance(elem, str):
        return True
    return False


def is_str_empty(elem: str) -> bool:
    """
    check if elem of type str is empty
    """
    return not elem


def is_image_path(path: str) -> bool:
    """
    check if image has a correct path. Have an extention of jpeg or jpg. If the image is not corrupted.
    """
    if not os.path.isfile(path):
        return False
    valid = {".jpg", ".jpeg"}
    _, ext = os.path.splitext(path)
    if ext.lower() not in valid:
        return False

    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except (IOError, SyntaxError):
        return False


def ft_load(path: str) -> Union[np.ndarray, list]:
    """
    if an error append return an empty array

    print shape of the image, height, width, and mode

    Return list of pixel in rgb.
    """
    try:
        assert is_str(path), "path must be an str"
        assert not is_str_empty(path), "path must not be empty"
        assert is_image_path(path), "path must be a valid image jpeg or jpg"
    except AssertionError as error:
        print(error)
        return []
    try:
        with Image.open(path) as img:
            height, width = img.size
            mode = img.mode
            if mode == "RGB":
                res = (height, width, 3)
                print(f"The shape of image is: {res}")
                info_img = np.array(img)
                return info_img
            else:
                new_img = img.convert("RGB")
                res = (height, width, 3)
                print(f"The shape of image is: {res}")
                return np.array(new_img)
    except (IOError, SyntaxError):
        return []


def main():
    print(ft_load("/mnt/nfs/homes/rkhelif/Downloads/landscape.jpg"))
    return


# your code here

if __name__ == "__main__":
    main()
