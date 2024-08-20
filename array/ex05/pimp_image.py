from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def display_image(img) -> None:
    """
    Display the image
    """
    plt.imshow(img)
    plt.show(block=False)
    plt.axis("off")
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.pause(10)
    plt.close()
    return


def ft_invert(arr: np.array) -> np.array:
    """
    Invert the color of the image
    """
    new_array = [[(255 - elem) for elem in sub_arr] for sub_arr in arr]
    new_array = np.array(new_array)
    new_image = Image.fromarray(new_array)
    print("The shape of the new image is: ", new_array.shape)
    print(new_array)
    print("inverts the color of the image")
    display_image(new_image)
    return


def ft_red(array) -> np.array:
    """
    Keep only the red color of the image
    """
    new_array = np.copy(array)
    for i in range(new_array.shape[0]):
        for j in range(new_array.shape[1]):
            if new_array[i][j][0] == 0:
                new_array[i][j][0] = 0
            new_array[i][j][1] = 0
            new_array[i][j][2] = 0
    new_image = Image.fromarray(new_array)
    print("The shape of the new image is: ", new_array.shape)
    print(new_array)
    print("Keep only the red color of the image")
    display_image(new_image)
    return


def ft_green(array) -> np.array:
    """
    Keep only the green color of the image
    """
    new_array = np.copy(array)
    for i in range(new_array.shape[0]):
        for j in range(new_array.shape[1]):
            if new_array[i][j][1] == 0:
                new_array[i][j][1] = 0
            new_array[i][j][0] = 0
            new_array[i][j][2] = 0
    new_image = Image.fromarray(new_array)
    print("The shape of the new image is: ", new_array.shape)
    print(new_array)
    print("Keep only the green color of the image")
    display_image(new_image)
    return


def ft_blue(array) -> np.array:
    """
    Keep only the blue color of the image
    """
    new_array = np.copy(array)
    for i in range(new_array.shape[0]):
        for j in range(new_array.shape[1]):
            if new_array[i][j][2] == 0:
                new_array[i][j][2] = 0
            new_array[i][j][0] = 0
            new_array[i][j][1] = 0
    new_image = Image.fromarray(new_array)
    print("The shape of the new image is: ", new_array.shape)
    print(new_array)
    print("Keep only the blue color of the image")
    display_image(new_image)
    return


def ft_grey(array) -> np.array:
    """
    Convert the image to a grey scale
    """
    new_array = np.copy(array)
    for i in range(new_array.shape[0]):
        for j in range(new_array.shape[1]):
            coefficients = np.array([0.299, 0.587, 0.114])
            y = np.dot(new_array[i][j], coefficients)
            new_array[i][j][0] = y
            new_array[i][j][1] = y
            new_array[i][j][2] = y

    new_image = Image.fromarray(new_array)
    print("The shape of the new image is: ", new_array.shape)
    print(new_array)
    print("Convert the image to a grey scale")
    display_image(new_image)
    return


def ft_display_image_regular(array) -> None:
    """
    Display the image
    """
    new_image = Image.fromarray(array)
    print("The shape of the new image is: ", array.shape)
    print(array)
    print("Display the image")
    display_image(new_image)
    return


def main():
    dataImageRgb = ft_load("landscape.jpg")
    print
    if isinstance(dataImageRgb, list):
        return
    try:
        ft_display_image_regular(dataImageRgb)
        ft_invert(dataImageRgb)
        ft_red(dataImageRgb)
        ft_green(dataImageRgb)
        ft_blue(dataImageRgb)
        ft_grey(dataImageRgb)
        return
    except KeyboardInterrupt:
        print("Process interupted by user.")
    return


if __name__ == "__main__":
    main()
