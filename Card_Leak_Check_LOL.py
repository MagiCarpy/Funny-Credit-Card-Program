import PySimpleGUI as sg
import time

def main_window():
    """
    Defines the layout and creates the window.

    This will allow you to "reuse" the layout.
    Of course, the layout isn't reused, it is creating a new copy of the layout
    every time the function is called.

    :return: newly created window
    :rtype: sg.Window
    """

    # ------------------- Layout Definition -------------------
    layout = [  [sg.Text('Card Number'), sg.InputText()],
            [sg.Text('Expire Date  '), sg.InputText()],
            [sg.Text('Pin              '), sg.InputText()],
            [sg.Button('Submit')] ]

    # ------------------- Window Creation -------------------
    return sg.Window('Credit Card Leak Check', layout)

def load_window():
    """
    Defines the layout and creates the window.

    This will allow you to "reuse" the layout.
    Of course, the layout isn't reused, it is creating a new copy of the layout
    every time the function is called.

    :return: newly created window
    :rtype: sg.Window
    """

    # ------------------- Layout Definition -------------------
    layout = [[sg.ProgressBar(100, key='-PROGRESS_BAR-')], 
           [sg.Button('Cancel', key='-Cancel-')]]

    # ------------------- Window Creation -------------------
    return sg.Window('Checking Databases', layout)

# Create the Window
window = main_window()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
        window.close()

    print(f'{values[0]} + {values[1]} + {values[2]}')
    progress = load_window()
    progress_count = 0
    while(progress_count <= 100):
        progress_count += 1
        pevent, _ = progress.read(timeout=0)
        progress['-PROGRESS_BAR-'].update(current_count=progress_count)
        time.sleep(0.025)
        if pevent == sg.WIN_CLOSED or pevent == '-Cancel-' or progress_count == 100:
            progress['-PROGRESS_BAR-'].update(current_count=0)
            if progress_count == 100:
                progress_count = 101
            progress.close()
            break
    if progress_count == 101:
        sg.Window('SUCCESS', [[sg.T('Your card was not found in any data leaks')]], disable_close=False).read(close=True)  

window.close()
