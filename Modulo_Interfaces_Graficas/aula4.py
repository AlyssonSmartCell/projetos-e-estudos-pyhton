
# A aula quatro consiste em criar uma tela com pysimplegui

import PySimpleGUI as sg

#Tema
sg.theme('DarkBlack')
#layout
layout = [
    [sg.Text('Digite seu nome')],
    [sg.Input(key='nome')],
    [sg.Text('Digite sua idade')],
    [sg.Input(key='idade')],
    [sg.Button(button_text='Cadastrar')],
]
#Janela
window = sg.Window('Tela de cadastro', layout=layout)
#Leitura de eventos e valores
while True:
    events,values = window.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Cadastrar': 
        r = values
         #print(f'Voce cadastrou '+ values[] +' com a idade '+ values[] '.')
        print(f"Voce cadastrou {r['nome']} com a idade {r['idade']}.")
        break
