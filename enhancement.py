import cv2
import numpy as np


def enhance_image(image, brightness=0, contrast=1.0):

    image = np.array(image)

    enhanced = cv2.convertScaleAbs(
        image,
        alpha=contrast,
        beta=brightness
    )

    return enhanced


def sharpen_image(image):

    image = np.array(image)

    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    sharpened = cv2.filter2D(image, -1, kernel)

    return sharpened