from pynput.mouse import Button, Controller

mouse = Controller()


def main():
    """This code snippet is using the mouse library to interact with the mouse on the computer. 
    It first reads the current position of the mouse pointer and prints it out. 
    It then sets the position of the mouse pointer to coordinates (10, 20) and prints out the new position. 
    The code then moves the mouse pointer relative to its current position by (5, -5). 
    After that, it performs a series of mouse actions, such as pressing and releasing the left mouse button, 
    double-clicking the left mouse button, and scrolling the mouse wheel down two steps.
    """
    # Read pointer position
    print(
        f'The current pointer position is {mouse.position}'
    )

    # Set pointer position
    mouse.position = (10, 20)
    print(
        f'The new pointer is moved to {mouse.position}'
    )

    # Move pointer relative to current position
    mouse.move(5, -5)

    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)

    # Double click; this is different from pressing and releasing
    # twice on Mac OSX
    mouse.click(Button.left, 2)

    # Scroll two steps down
    mouse.scroll(0, 2)


if __name__ == '__main__':
    main()
