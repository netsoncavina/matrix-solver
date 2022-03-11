from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Dark grey 9')
layout = [
    [sg.Input(key = 'a1', size=(20,20), justification="center"), sg.Text('x'), sg.Input(key = 'a2', size=(20,20), justification="center"), sg.Text('y'), sg.Input(key = 'a3', size=(20,20), justification="center"), sg.Text('z'), sg.Text('='), sg.Input(key = 'a4', size=(20,20), justification="center")],
    [sg.Input(key = 'b1', size=(20,20), justification="center"), sg.Text('x'), sg.Input(key = 'b2', size=(20,20), justification="center"), sg.Text('y'), sg.Input(key = 'b3', size=(20,20), justification="center"), sg.Text('z'), sg.Text('='), sg.Input(key = 'b4', size=(20,20), justification="center")],
    [sg.Input(key = 'c1', size=(20,20), justification="center"), sg.Text('x'), sg.Input(key = 'c2', size=(20,20), justification="center"), sg.Text('y'), sg.Input(key = 'c3', size=(20,20), justification="center"), sg.Text('z'), sg.Text('='), sg.Input(key = 'c4', size=(20,20), justification="center")],
    [sg.Button('Calcular', size=(10,1), ), sg.Button('Limpar', size=(10,1))],
    [sg.Text("x = "), sg.Text('',key="outputX")],
    [sg.Text("y = "), sg.Text('',key="outputY")],
    [sg.Text("z = "), sg.Text('',key="outputZ")]
]

# Window
window = sg.Window('Calculo de incognitas', layout, resizable=False)

# Event listener
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    
       