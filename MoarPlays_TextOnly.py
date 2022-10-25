import cv2
import numpy as np
import pytesseract
import time
import vgamepad as vg

#Set PATH for Tesseract - This will change per machine
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
gamepad = vg.VX360Gamepad()

# We only need the ImageGrab class from PIL
from PIL import ImageGrab

# Run forever unless you press Esc
oldconvert = "Hello"
while True:
    # select what area of the screen to capture (x,y to x,y)
    cap = ImageGrab.grab(bbox=(1338 , 847, 1503, 871))

    # Convert the image into a numpy array
    cap_arr = np.array(cap)

    # Shows a preview of the capture area for debug purposes, disable on lowend systems
    cv2.imshow("", cap_arr)


    # Find text in the image and write to variable of 'text'
    text = pytesseract.image_to_string(cap)

    # This just removes spaces from the beginning and ends of text to make it more clean
    text = text.strip()

    # If any text was translated from the image, print it
    if len(text) > 0:
        print(text)

    # Converts all text to lowercase for input selection
    convert = text.lower()

    # Checks if the command has already been issued, skips duplicate commands
    if convert != oldconvert:

        if "fast" in str(convert):
            gamepad.right_trigger(value=255)
            gamepad.left_trigger(value=0)
            gamepad.update()

        if "slow" in str(convert):
            gamepad.left_trigger(value=255)
            gamepad.right_trigger(value=0)
            gamepad.update()

        if "left" in str(convert):
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        if "right" in str(convert):
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if "up" in str(convert):
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-5.0)
            gamepad.update()
            time.sleep(1)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
            gamepad.update()

        if "down" in str(convert):
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=5.0)
            gamepad.update()
            time.sleep(1)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
            gamepad.update()

        if "rollr" in str(convert):
            gamepad.left_joystick_float(x_value_float=0.7, y_value_float=0.0)
            gamepad.update()
            time.sleep(1)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
            gamepad.update()

        if "rolll" in str(convert):
            gamepad.left_joystick_float(x_value_float=-0.7, y_value_float=0.0)
            gamepad.update()
            time.sleep(1)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
            gamepad.update()

        if "reset" in str(convert):
            gamepad.reset()
            gamepad.update()

    # Updates the old message store
    oldconvert = convert
    # This line will break the while loop when you press Esc
    if cv2.waitKey(1) == 27:
        break

# This will make sure all windows created from cv2 is destroyed
cv2.destroyAllWindows()