from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def zoom(img: np.array, hw: tuple):
    """
    take an np:array of data and zoom to the picture
    a picture of the zoom photo will apear during 60 secondes
    on the picture you can see coordinate of the photo
    """
    height, width, _ = img.shape
    new_height, new_width = hw
    start_x = (width // 2) - (new_width // 2)
    start_y = (height // 2) - (new_height // 2)
    end_x = start_x + new_width
    end_y = start_y + new_height

    crop_image = img[start_y:end_y, start_x:end_x]

    new_image = Image.fromarray(crop_image)

    light_image = new_image.convert("L")
    array_3d = np.expand_dims(light_image, axis=-1)

    print(f"New shape after slicing: {array_3d.shape}")
    print(array_3d)
    plt.imshow(array_3d[:, :, 0], cmap="gray")
    plt.show(block=False)
    plt.pause(60)
    plt.close()
    return


def main():
    dataImageRgb = ft_load("/mnt/nfs/homes/rkhelif/Downloads/animal.jpeg")
    if isinstance(dataImageRgb, list):
        return
    try:
        zoom(dataImageRgb, (400, 400))
    except KeyboardInterrupt:
        print("Process interupted by user.")
        plt.close("all")
    return


if __name__ == "__main__":
    main()
