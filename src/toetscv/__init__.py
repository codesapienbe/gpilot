from pynput.keyboard import Key, Controller
from time import sleep
import os
import sys
import datetime
import time

# import computer vision functions
import cv2
import mediapipe as mp

keyboard = Controller()

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)


def show(camera):
    _, frame = camera.read()
    cv2.imshow('frame', frame)
    return frame


def listen_keys(camera, frame):
    k = cv2.waitKey(1)
    if k == 27:
        destroy(camera)
    elif k == ord('s'):
        save_cv(camera, frame, f'{datetime.datetime.now()}.png')


def destroy(camera):
    camera.release()
    cv2.destroyAllWindows()


def save(camera, frame, filename):
    cv2.imwrite(filename, frame)
    destroy(camera)


def run_bash():
    # start win+r key
    keyboard.press(Key.cmd_r)
    keyboard.release(Key.cmd_r)

    sleep(0.5)

    # start bash with typing command "bash"
    keyboard.type("bash")

    sleep(0.5)

    # press enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    sleep(0.5)


def run_ls():
    # type "ls"
    keyboard.type("ls")

    sleep(0.5)

    # press enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    sleep(0.5)


def run_pip(package_name):
    # type "exit"
    keyboard.type(f"pip install --upgrade {package_name}")

    sleep(0.5)

    # press enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    sleep(0.5)


def main():
    """
    Presses the win+r key combination, types "bash" to start a bash terminal,
    types "ls" to list files, types "exit" to exit the terminal. No parameters
    or return types.
    """

    run_bash()

    run_ls()

    run_pip('gpilot')

    while camera.isOpened():
        frame = show(camera)
        listen_keys(camera, frame)


if __name__ == '__main__':
    main()
