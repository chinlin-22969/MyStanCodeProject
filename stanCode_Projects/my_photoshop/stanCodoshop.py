"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = ((pixel.red - red)**2 + (pixel.green - green)**2 + (pixel.blue - blue)**2)**0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    red = 0
    green = 0
    blue = 0
    rgb = []
    for pixel in pixels:
        red += pixel.red
        green += pixel.green
        blue += pixel.blue
    rgb.append(red//len(pixels))
    rgb.append(green//len(pixels))
    rgb.append(blue//len(pixels))
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance",
    which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    dist_index_lst = []
    index = 0
    for pixel in pixels:
        dist = get_pixel_dist(pixel, get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2])
        dist_index_lst.append((dist, index))
        # store each pixel's color distance and index into Tuple and add it into the list
        # ex: [(dist, pixel_index), (dist1, pixel_index1), (dist2, pixel_index2)....]
        index += 1
    best = pixels[min(dist_index_lst)[1]]
    # best pixel is the tuple with the smallest-valued color distance among the other tuples in the list
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(result.width):
        for y in range(result.height):
            result_pixel = result.get_pixel(x, y)
            # to store the same location of pixel in each image, ex: [jpg1-pixel, jpg2-pixel, jpg3-pixel....]
            pixels = []
            for image in images:
                pixel = image.get_pixel(x, y)
                pixels.append(pixel)
            # get the best pixel among each images' pixel
            best_pixel = get_best_pixel(pixels)
            # fill the best pixels to the result image
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):  # os.listdir()可以讀取括弧內資料夾名稱內所有的檔案
        if filename.endswith('.jpg'):  # 找出此資料夾內所有endswith'jpg'的檔案
            filenames.append(os.path.join(dir, filename))  # 把後面的兩個args中間加上'/'成為一個合理的檔案路徑（path）
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]   # 取terminal裏面檔名後所有的token
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
