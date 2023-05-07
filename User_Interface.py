import PySimpleGUI as sg
import os
import easygui

def modify_variable(file_path, samples):
    if file_path:
        # Read the content of the original file
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Modify the line containing "samples = "
        modified_lines = []
        for line in lines:
            if "samples = " in line:
                modified_lines.append(f"samples = {samples}\n")
            else:
                modified_lines.append(line)

        # Specify the file name and location for the modified file
        file_dir, file_name = os.path.split(file_path)
        new_file_name = f"modified_{file_name}"

        # Create a new file path for the modified file
        file_extension = ".py"
        save_file_path = easygui.filesavebox("Save File As", default=f"{new_file_name}{file_extension}", filetypes=["*.py"])

        if save_file_path:
            # Make sure the file extension is .py
            save_file_path = os.path.splitext(save_file_path)[0] + file_extension

            # Save the modified content to the specified file path
            with open(save_file_path, 'w') as f:
                f.writelines(modified_lines)

            sg.popup(f"File saved successfully as {save_file_path}")
    else:
        sg.popup("No file has been uploaded.")

# Define the GUI layout
layout = [
    [sg.Text('Select a Python file to upload:')],
    [sg.Input(key='-FILE-', enable_events=True, readonly=True), sg.FileBrowse(file_types=(("Python Files", "*.py"),))],
    [sg.Text('Number of environmental samples (1 to 72):')],
    [sg.Input(key='-SAMPLES-', size=(45, 1))],
    [sg.Button('Save', size=(10, 1)), sg.Text(' ' * 50), sg.Button('Exit', size=(10, 1), button_color=('white', 'red'))]
]

window = sg.Window('File Modifier', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == '-FILE-':
        file_path = values['-FILE-']
        sg.popup(f'File uploaded: {file_path}')

    if event == 'Save':
        file_path = values['-FILE-']
        samples = values['-SAMPLES-']

        if not samples.isdigit() or not 1 <= int(samples) <= 72:
            sg.popup('Please enter a valid number of environmental samples (1 to 72).')
        else:
            modify_variable(file_path, int(samples))

window.close()
