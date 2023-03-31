import PySimpleGUI as sg
import os.path

info_column = [
    
        [sg.Text("Enter data")],
        [sg.Text('Pregnancies', size=(20,1)), sg.InputText(key='pregnancies')],
        [sg.Text('Glucose', size=(20,1)), sg.InputText(key='glucose')],
        [sg.Text('Blood Pressure', size=(20,1)), sg.InputText(key='bloodPressure')],
        [sg.Text('Skin Thickness', size=(20,1)), sg.InputText(key='skinThickness')],
        [sg.Text('Insulin', size=(20,1)), sg.InputText(key='insulin')],
        [sg.Text('BMI', size=(20,1)), sg.InputText(key='bmi')],
        [sg.Text('Diabetes Pedigree Function', size=(20,1)), sg.InputText(key='dpf')],
        [sg.Text('Age', size=(20,1)), sg.InputText(key='age')],
        [sg.Button(button_text='Predict'), sg.Text(text='', key='_RESULT_')]
    
]

# ----- Full layout -----

layout = [

    [
        sg.Column(info_column)
    ]

]