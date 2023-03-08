import PySimpleGUI as sg  

status = True
while status == True:
#Thema
    sg.theme("Dark Blue 3")

#Layout

    layout = [
        [sg.Text('Produto',size=(10,1)), sg.Input(key='Produto',size=(25,1))],
        [sg.Text('Preço',size=(10,1)), sg.Input(key='preço',size=(25,1))],
        [sg.Text('Quantidade',size=(10,1)), sg.Input(key='Quantidade',size=(25,1))],
        [sg.Button('Cadastrar')],
    ]

#window
    window = sg.Window('Tela de cadastro', layout=layout)

#eventos
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'cancelar':
        break
    elif event == 'Cadastrar':
        r= values
        sg.popup(f'Voce cadastrou o produto '+r['Produto']+' com preço de R$'+r['preço']+',00 em quantidade de '+r['Quantidade']+' unidades.')
        with open('Produtos.txt','a') as arquivo:
            for produto in r:
                arquivo.write(str(produto)+ (',')+ ('\n') )
        break
        