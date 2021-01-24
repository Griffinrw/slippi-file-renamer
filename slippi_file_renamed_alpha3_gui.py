# this is the gui file to go with the logic

import PySimpleGUI as sg
import slippi_file_renamer_alpha3 as renamer

directory = sg.popup_get_folder('Enter the directory that contains your slippi files you\'d like to rename')
sg.popup('You entered', directory) #, 'is this correct?')


'''sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()'''








if __name__ == '__main__':
    renamer.rename_slippi_files(directory)

