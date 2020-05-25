import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
from numpy import asarray
import time
#hi harshit

def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for cactus
    for i in range(483, 488):
        for j in range(398, 425):
            if data[i, j] < 100:
                hit("up")
                return

    # Draw the rectangle for birds
    for i in range(483, 488):
        for j in range(370, 397):
            if data[i, j] < 100:
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



        # print(asarray(image))
        
        # # Draw the rectangle for birds
        # for i in range(483, 488):
        #     for j in range(370, 397):
        #         data[i, j] = 171
        
        # # Draw the rectangle for cactus
        # for i in range(483, 488):
        #     for j in range(398, 425):
        #         data[i, j] = 255
        
        # image.show()
        # break

