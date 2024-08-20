from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def rotate_90_degrees(matrix):
    """
    rotate the picture to 90 degree
    """
    rows = len(matrix)
    cols = len(matrix[0])
    new_array = []

    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[rows - 1 - row][col])
        new_array.append(new_row)
    return new_array


def rotate(img: np.array, hw: tuple):
    """
    take an np:array of data and rotate the picture to 270 degree
    a picture of the photo will apear during 60 secondes
    on the picture you can see coordinate of the photo
    """
    height, width, _ = img.shape
    new_height, new_width = hw
    start_x = (width // 2) - (new_width // 2)
    start_y = (height // 2) - (new_height // 2)
    end_x = start_x + new_width
    end_y = start_y + new_height

    crop_image = img[start_y:end_y, start_x:end_x]
    transposed = crop_image
    for k in range(3):
        transposed = rotate_90_degrees(transposed)

    transposed = np.array(transposed)
    print(transposed)
    new_image = Image.fromarray(transposed)

    light_image = new_image.convert("L")

    array_3d = np.expand_dims(light_image, axis=-1)

    print(f"The shape of image is: {array_3d.shape}")
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
        rotate(dataImageRgb, (400, 400))
        return
    except KeyboardInterrupt:
        print("Process interupted by user.")
        plt.close("all")
    return


if __name__ == "__main__":
    main()
