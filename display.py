import curses

testTextArray = ["  System Hardware Information     ",
                  "     CPU Model: Intel Something", "     CPU Core: 1000"]

def terminalDisplay(stdscr, displayStrings=None):
    # Initialize curses
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    # Calculate box dimensions
    maxY, maxX = stdscr.getmaxyx()
    boxHeight = maxY - 2
    boxWidth = maxX - 2

    # Create a box
    box = curses.newwin(boxHeight, boxWidth, 1, 1)
    box.box()

    if displayStrings is not None:
        # Display the provided strings inside the box
        for i, string in enumerate(displayStrings):
            box.addstr(i + 1, 1, string)

    box.refresh()

    # Wait for user to press Enter
    stdscr.addstr(maxY - 1, 0, "Press Enter to exit...")
    stdscr.refresh()

    # Wait for the Enter key to be pressed
    while True:
        key = stdscr.getch()
        if key == ord('\n'):  # Check for Enter key press
            break



"""
# Run the terminalDisplay function
curses.wrapper(terminalDisplay, testTextArray)

"""