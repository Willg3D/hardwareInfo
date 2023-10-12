"""
Display a list of strings in a text box format.

Args:
array of strings # can be empty array

Tests (empty, single line, mutiple lines)
>>> empty_strings = []
>>> terminalDisplay(empty_strings)  # No output as there are no strings to display

>>> single_string = ["Single Line"]
>>> terminalDisplay(single_string)
╔═════════════╗
║ Single Line ║
╚═════════════╝

>>> strings = ["Hello", "World!"]
>>> terminalDisplay(strings)
╔════════╗
║ Hello  ║
║ World! ║
╚════════╝
"""
def terminalDisplay(displayStrings = None):
    if not displayStrings:
        return

    maxLength = max(len(i) for i in displayStrings)
    boxWidth = maxLength + 2
    rowLine = '═' * boxWidth

    print('╔' + rowLine + '╗')
    for string in displayStrings:
        formattedString = f'║ {string:{maxLength}} ║'
        print(formattedString)
    print('╚' + rowLine + '╝')


if __name__ == "__main__":
    import doctest
    doctest.testmod()