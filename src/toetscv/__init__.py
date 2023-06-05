from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardCtrl
from pynput.mouse import Button, Controller as MouseCtrl
from time import sleep
import os
import sys
import datetime
import time

# import computer vision functions
import cv2
import mediapipe as mp


def show(camera):
    """Displays the video frame captured by the camera and returns the frame.

    :param camera: A camera object which captures the video frame.
    :return: Returns the video frame captured by the camera.
    """
    _, frame = camera.read()
    cv2.imshow('frame', frame)
    return frame


def press_key(keyboard, key):
    """Presses the specified key.
    """
    keyboard.press(key)
    keyboard.release(key)
    sleep(0.5)


def press_keys(keyboard, keys):
    """Presses the specified keys.
    """
    for key in keys:
        press_key(keyboard, key)


def listen_keys(camera, frame):
    """Listens for keyboard inputs and performs specific actions based on the input.

    Args:
        camera: A cv2.VideoCapture object representing the camera.
        frame: A frame captured by the camera.

    Returns:
        None
    """
    k = cv2.waitKey(1)
    if k == 27:
        destroy(camera)
    elif k == ord('s'):
        save_cv(camera, frame, f'{datetime.datetime.now()}.png')


def destroy(camera):
    """Releases the specified camera and destroys all associated windows.

    :param camera: A cv2 camera object.
    :return: None.
    """
    camera.release()
    cv2.destroyAllWindows()


def save(camera, frame, filename):
    """Saves a frame from a camera to a file with the given filename. 
    The function takes in three parameters: 
        camera: the camera object
        frame: the frame to be written to the file
        filename: the path and name of the file to be written
    The function does not return anything. It calls the destroy function to release the camera resources.
    """
    cv2.imwrite(filename, frame)
    destroy(camera)


def recognize_hands(frame):
    """Recognizes hands in the frame.
    """
    with mp.solutions.hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        results = hands.process(frame)
        return results


def run_bash(keyboard):
    """Runs a bash terminal by simulating key presses. 

    The function does not take any parameters or return any values.
    It simulates key presses to open the start menu ('win+r' keys), types 'bash' to open the bash terminal, 
    and presses the enter key to execute the command.
    """
    press_key(keyboard, Key.cmd_r)

    # start bash with typing command "bash"
    keyboard.type("bash")

    sleep(0.5)

    # press enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    sleep(0.5)


def run_ls(keyboard):
    """Runs the "ls" command by simulating keyboard input.
    This function takes no parameters and does not return anything.
    """
    # type "ls"
    keyboard.type("ls")

    sleep(0.5)

    press_key(keyboard, Key.enter)


def run_pip(keyboard, package_name):
    """Runs pip to install or upgrade a specified package.

    :param package_name: A string representing the name of the package to be installed or upgraded.
    :return: None
    """
    # type "exit"
    keyboard.type(f"pip install --upgrade {package_name}")

    sleep(0.5)

    press_key(keyboard, Key.enter)


def move_mouse(mouse, x, y):
    """Moves the mouse to the specified coordinates.
    """
    mouse.position = (x, y)


def right_click(mouse):
    """Right clicks the mouse.
    """
    mouse.click(Button.right, 1)


def left_click(mouse):
    """Left clicks the mouse.
    """
    mouse.click(Button.left, 2)


def middle_click(mouse):
    """Middle clicks the mouse.
    """
    mouse.click(Button.middle, 1)


def zoom_in(mouse, keyboard):
    """Zooms in the mouse.
    """
    keyboard.press(Key.ctrl)
    mouse.scroll(0, 100)
    keyboard.release(Key.ctrl)


def zoom_out(mouse, keyboard):
    """Zooms out the mouse.
    """
    keyboard.press(Key.ctrl)
    mouse.scroll(0, -100)
    keyboard.release(Key.ctrl)


def main():
    """
    Presses the win+r key combination, types "bash" to start a bash terminal,
    types "ls" to list files, types "exit" to exit the terminal. No parameters
    or return types.
    """

    keyboard = KeyboardCtrl()
    mouse = MouseCtrl()

    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
    camera.set(cv2.CAP_PROP_FPS, 30)
    camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)

    # run_bash(keyboard)
    # run_ls(keyboard)
    # run_pip(keyboard, 'gpilot')

    while camera.isOpened():

        frame = show(camera)
        hands = recognize_hands(frame)

        if hands.multi_hand_landmarks:
            for hand in hands.multi_hand_landmarks:
                for id, lm in enumerate(hand.landmark):
                    print(id, lm)
                    # move the mouse to the center of the hand
                    move_mouse(mouse, lm.x, lm.y)

        listen_keys(camera, frame)


if __name__ == '__main__':
    main()
