import curses, time

def rin(stdscr):
    """checking for keypress"""
    stdscr.keypad(True)
    stdscr.nodelay(True)  # do not wait for input when calling getch
    return stdscr.getch()

while True:
    print("key:", curses.wrapper(rin)) # prints: 'key: 97' for 'a' pressed
    time.sleep(1)
                                        # '-1' on no presses

