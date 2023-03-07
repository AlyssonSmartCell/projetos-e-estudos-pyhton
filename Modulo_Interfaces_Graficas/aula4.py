
# A aula quatro consiste em criar uma tela com pysimplegui

import PySimpleGUI as sg

#Tema
sg.theme('DarkBlack')
#layout
layout = [
    [sg.Text('Digite seu nome')],
    [sg.Input()],
    [sg.Text('Digite sua idade')],
    [sg.Input()],
    [sg.Button('Cadastrar')],
]
#Janela
window = sg.Window('Tela de cadastro', layout=layout)
#Leitura de eventos e valores
while True:
    events,values = window.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Cadastrar':
        print(f'Voce cadastrou {layout[0,1]} com a idade {layout[0,3]}.')
