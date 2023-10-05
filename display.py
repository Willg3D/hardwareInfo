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

"""

testTextArray = ["System Hardware Information",
                  "CPU Model: Intel Something", "CPU Core: 1000"]

terminalDisplay(testTextArray)

"""