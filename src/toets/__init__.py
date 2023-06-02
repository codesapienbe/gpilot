from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()


def main():
    """
    Presses the win+r key combination, types "bash" to start a bash terminal,
    types "ls" to list files, types "exit" to exit the terminal. No parameters
    or return types.
    """
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

    # type "ls"
    keyboard.type("ls")

    sleep(0.5)

    # press enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    sleep(0.5)

    # type "exit"
    keyboard.type("exit")

    sleep(0.5)


if __name__ == '__main__':
    main()
