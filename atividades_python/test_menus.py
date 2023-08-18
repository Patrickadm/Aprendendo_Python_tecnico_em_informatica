import PySimpleGUI as sg
import sqlite3 as bbb

#cria a conexão e interage com o banco
conn = bbb.connect("Desktop/bd_clientes/clientes.db") #Conecta ao banco , deve-se colocar o caminho da pasta principal
c = conn.cursor()

#Criar o layout
layout = [
    [sg.Menu([
    ["Cadastrar", ('Cadastro Clientes', 'Cadastro Fornecedores', 'Cadastro Transportadoras')],
    ["Consulta", ('Consulta Clientes', 'Cnsulta Fornecedores', 'Consulta Transportadoras')],
    ["Relatório", ('Relatório Clientes', 'Relatório Fornecedores', 'Relatório Transportadoras')]
    ],
    tearoff=False)]
]

#Criar a janela principal e chamar os componentes desta na janela
# WINDOW (nome da janela, componentes, tamanho da janela)
# MUDAR A FONTE E HABILITAR O BOTÃO MAXIMIZAR: font=font_programa,resizable=True
window = sg.Window("Sistema de vendas 1.0",layout,size=(600,400))


#Se o programa for executado, abra a janela
#While janela principal
while True:
    event, values = window.read()

    #SE a janela for fechada
    if event == sg.WINDOW_CLOSED:
        break








    if event == "Cadastro Clientes":

        #criar layout
        cadastro_layout = [
            [sg.Text("Produto")],      
            [sg.InputText(key="produto")],
            [sg.Text("Valor")],      
            [sg.InputText(key="valor")],
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]

        cadastro_window = sg.Window("Cadastro de produtos", cadastro_layout, size=(400,200))




        #While do cadastro
        while True:
            event, values = cadastro_window.read()
     
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_window.close()
                break


            #interagindo com o banco
            c.execute("INSERT INTO vendas (produto, valor) VALUES (?, ?)", (values["produto"], values["valor"]))
            conn.commit()

            #Limpar iputs após o cadastro
            cadastro_window["produto"].update("")
            cadastro_window["valor"].update("")

            #Confirmar o cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

        cadastro_window.close()
        

    elif event == "Consulta":
    
            consulta_layout =[
                [sg.Text("Produto")],
                [sg.InputText(key="produto")],
                [sg.Button("Consultar")],
                [sg.Button("Cancelar")],
                [sg.Table(values=[], headings=["produto","valor"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")]
            ]    
            consulta_window = sg.Window("Consulta de produtos", consulta_layout, resizable=True)

        #loop eventos
        
            while True:
                event, values = consulta_window.read()
            
                if event == sg.WIN_CLOSED or event == "Cancelar":
                    consulta_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["produto"].upper()
                c.execute( "SELECT produto, valor FROM vendas WHERE UPPER(produto) = ?",(produto_busca,))
                registros = c.fetchall()

                # ATUALIZAR
                tabela = consulta_window["tabela"]
                tabela.update(values=registros)     
                       
            consulta_window.close()                        


conn.close() 
