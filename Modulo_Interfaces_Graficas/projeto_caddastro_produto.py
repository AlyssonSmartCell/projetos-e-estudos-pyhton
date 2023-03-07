import PySimpleGUI as sg  

#Thema
sg.theme("Dark Blue 3")

#Layout

layout = [
    [sg.Text('Produto',size=(10,1)), sg.Input(key='Produto',size=(25,1))],
    [sg.Text('sla')],
    [],
    [],

]

#window
window = sg.Window('Tela de cadastro', layout=layout)

#eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'cancelar':
        break
