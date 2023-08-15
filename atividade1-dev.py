
import PySimpleGUI as sg
import sqlite3 as banco
# INICIANDO A CONEXÂO COM O BANCO DE DADOS
conn = banco.connect("DESKTOP/clientes.db")
c = conn.cursor()


# BOTÂO DO MENU PRINCIPAL COM A OPÇÂO DE CADASTRAR
sg.theme("DarkTeal12")
layout = [
    [sg.Button("Cadastrar", size=(20, 2), font=("Arial", 12))],
    
]

# NOME QUE APARECE NO SISTEMA E DEFINIÇÂO DO TAMANHO DA TELA  
window = sg.Window("Sistema de Cadastro Vs.1.0",layout,resizable=True) 

while True:
    event, values = window.read()

    #SE a janela for fechada Encerra o Processo de cadastro
    if event == sg.WINDOW_CLOSED:
        break







    #CADASTRO DE CLIENTES

    if event == "Cadastrar":

        #criar layout da seguna tela que aparece quando clica em cadastrar cliente
        cadastro_layout = [
            [sg.Text("Nome")],      
            [sg.InputText(key="nome")],
            [sg.Text("CPF")],      
            [sg.InputText(key="cpf")],
            [sg.Text("Endereço")],      
            [sg.InputText(key="endereco")],
            [sg.Text("Telefone")],      
            [sg.InputText(key="telefone")],
            [sg.Text("Cidade")],      
            [sg.InputText(key="cidade")],
            [sg.Text("Estado")],      
            [sg.InputText(key="estado")],                       
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]
            

        cadastro_window = sg.Window("Cadastro de Clientes", cadastro_layout, size=(400,500))

         #While da janela de  cadastro de clientes
        while True:
            event, values = cadastro_window.read()
     
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_window.close()
                break


            #interagindo com o banco
            c.execute("INSERT INTO clientes (nome, cpf, endereco, telefone, cidade, estado) VALUES (?, ?, ?, ?, ?, ?)", (values["nome"], values["cpf"],values["endereco"],values["telefone"],values["cidade"],values["estado"]))
            conn.commit()

            #Limpar iputs após o cadastro
            cadastro_window["nome"].update("")
            cadastro_window["cpf"].update("")
            cadastro_window["endereco"].update("")
            cadastro_window["telefone"].update("")
            cadastro_window["cidade"].update("")
            cadastro_window["estado"].update("")

            #Confirmar o cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

        cadastro_window.close()
