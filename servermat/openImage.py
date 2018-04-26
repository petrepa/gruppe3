import cv2
#import screeninfo
from pynput.keyboard import Key, Controller



def displayImage(image):
    screen_id = 0
    is_color = False
    keyboard = Controller()
    width = 1680
    height = 1050
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    picture = image + '.jpg' 
    pic = cv2.imread(picture, 1)

    window_name = 'Bilde'

    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(window_name, 1681, 0)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)
    cv2.imshow(window_name, image)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    

#picture = 'test.jpg'
#displayImage(picture)
