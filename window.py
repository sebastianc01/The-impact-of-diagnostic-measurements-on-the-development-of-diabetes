import PySimpleGUI as sg
import biai
import windowinfo
import string

# returns True when passed string can be converted to int or float, False otherwise
def isNumber(number: string):
    try:
        float(number)
        return True
    except ValueError:
        return False
        
# function checks correctness of the input data
def checkInputs(window, values):
    correct = True
    if not values['pregnancies'].isnumeric():
        window['pregnancies'].Update('')
        correct = False
    if not values['glucose'].isnumeric():
        window['glucose'].Update('')
        correct = False
    if not values['bloodPressure'].isnumeric():
        window['glucose'].Update('')
        correct = False
    if not values['skinThickness'].isnumeric():
        window['skinThickness'].Update('')
        correct = False
    if not values['insulin'].isnumeric():
        window['insulin'].Update('')
        correct = False
    if not isNumber(values['bmi']):
        window['bmi'].Update('')
        correct = False
    if not isNumber(values['dpf']):
        window['dpf'].Update('')
        correct = False
    if not values['age'].isnumeric():
        window['age'].Update('')
        correct = False
    if not correct:
        return False
    else:
        return True

# predicts the result
def predict(neuralNetwork: biai.NeuralNetwork, window, values):
    prediction = neuralNetwork.getModel().predict([[
        int(values['pregnancies']),
        int(values['glucose']),
        int(values['bloodPressure']),
        int(values['skinThickness']),
        int(values['insulin']),
        float(values['bmi']),
        float(values['dpf']),
        int(values['age'])
    ]])
    result =  "Diabetes" if prediction[0][0] > 0.5 else "Healthy"
    
    result = result + '(' + str(prediction[0][0]) + ')'
    window['_RESULT_'].Update(result)

window = sg.Window("Image Viewer", windowinfo.layout)
nn = biai.NeuralNetwork(21, "model")

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    print(values)
    if checkInputs(window, values):
        predict(nn, window, values)
    else:
        window['_RESULT_'].Update('')
    