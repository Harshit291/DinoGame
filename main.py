import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for cactus
    for i in range(483, 488):
        for j in range(228, 255):
            if data[i, j] > 170:
                hit("up")
                return

    # Draw the rectangle for birds
    for i in range(483, 488):
        for j in range(200, 227):
            if data[i, j] > 170:
                hit("down")
                return

    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)



        # # print(asarray(image))
        #
        # # Draw the rectangle for birds
        # for i in range(483, 488):
        #     for j in range(200, 227):
        #         data[i, j] = 171
        #
        # # Draw the rectangle for cactus
        # for i in range(483, 488):
        #     for j in range(228, 255):
        #         data[i, j] = 255
        #
        # image.show()
        # break

