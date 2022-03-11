from PySimpleGUI import PySimpleGUI as sg
from funcoes import *

# Layout
sg.theme('Dark grey 9')
layout = [
    [sg.Input(key = 'a1', size=(20,20), justification="center"), sg.Text('x'), sg.Input(key = 'a2', size=(20,20), justification="center"), sg.Text('y'), sg.Input(key = 'a3', size=(20,20), justification="center"), sg.Text('z'), sg.Text('='), sg.Input(key = 'a4', size=(20,20), justification="center")],
    [sg.Input(key = 'b1', size=(20,20), justification="center"), sg.Text('x'), sg.Input(key = 'b2', size=(20,20), justification="center"), sg.Text('y'), sg.Input(key = 'b3', size=(20,20), justification="center"), sg.Text('z'), sg.Text('='), sg.Input(key = 'b4', size=(20,20), justification="center")],
    [sg.Input(key = 'c1', size=(20,20), justification="center"), sg.Text('x'), sg.Input(key = 'c2', size=(20,20), justification="center"), sg.Text('y'), sg.Input(key = 'c3', size=(20,20), justification="center"), sg.Text('z'), sg.Text('='), sg.Input(key = 'c4', size=(20,20), justification="center")],
    [sg.Button('Calcular', size=(10,1), ), sg.Button('Limpar', size=(10,1)), sg.Text('Precisão decimal'), sg.Input('3',key = 'decimal', size=(5,20))],
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
    if events == "Calcular":
        x, y, z = calculaDeterminantes(float(values['a1']), float(values['a2']), float(values['a3']), float(values['a4']), float(values['b1']), float(values['b2']), float(values['b3']), float(values['b4']), float(values['c1']), float(values['c2']), float(values['c3']), float(values['c4']), int(values['decimal']))
        window.Element('outputX').Update(x)
        window.Element('outputY').Update(y)
        window.Element('outputZ').Update(z)
    if events == "Limpar":
        window.Element('a1').Update('')
        window.Element('a2').Update('')
        window.Element('a3').Update('')
        window.Element('a4').Update('')
        window.Element('b1').Update('')
        window.Element('b2').Update('')
        window.Element('b3').Update('')
        window.Element('b4').Update('')
        window.Element('c1').Update('')
        window.Element('c2').Update('')
        window.Element('c3').Update('')
        window.Element('c4').Update('')
        window.Element('outputX').Update('')
        window.Element('outputY').Update('')
        window.Element('outputZ').Update('')
        window.Element('outputX').Update('')
        window.Element('outputY').Update('')
        window.Element('outputZ').Update('')

       