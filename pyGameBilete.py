# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:44:27 2017

@author: sakurai
"""


import numpy as np
import cv2
import screeninfo


if __name__ == '__main__':
    screen_id = 0
    is_color = False

    # get the size of the screen
    screen = screeninfo.get_monitors()[screen_id]
    width, height = screen.width, screen.height

    # create image
    image = cv2.imread('test.jpg', 1)

    window_name = 'projector'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()