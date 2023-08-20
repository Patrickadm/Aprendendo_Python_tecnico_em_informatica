import PySimpleGUI as sg
import sqlite3 as banco
# INICIANDO A CONEXÂO COM O BANCO DE DADOS
conn = banco.connect("C:/Users/patri/OneDrive/Área de Trabalho/DataBase/clientes.db")
c = conn.cursor()
   
   
    

# BOTÂO DO MENU PRINCIPAL COM A OPÇÂO DE CADASTRAR
  

# Definir tema e layout do menu principal
# MENU COM BOTOÔES 
sg.theme("DarkTeal12")
layout = [
    [sg.Menu([
    ["Cadastrar", ('Cadastro Clientes', 'Cadastro Fornecedores', 'Cadastro Transportadoras')],
    ["Consulta", ('Consulta Clientes', 'Consulta Fornecedores', 'Consulta Transportadoras')],
    ["Relatório", ('Relatório Clientes', 'Relatório Fornecedores', 'Relatório Transportadoras')]
    ],
    tearoff=False)]
]





# NOME QUE APARECE NO SISTEMA E DEFINIÇÂO DO TAMANHO DA TELA  
window = sg.Window("Sistema de Cadastro Vs.1.0",layout,size=(300,200) )

while True:
    event, values = window.read()

    #SE a janela for fechada Encerra o Processo de cadastro
    if event == sg.WINDOW_CLOSED:
        break







    #CADASTRO DE CLIENTES

    if event == "Cadastro Clientes":

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





#CADASTRO DE FORNECEDORES

    elif event == "Cadastro Fornecedores":

        #criar layout da seguna tela que aparece quando clica em cadastrar cliente
        fornecedor_layout = [
            [sg.Text("Nome")],      
            [sg.InputText(key="nome")],
            [sg.Text("CNPJ")],      
            [sg.InputText(key="cnpj")],
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
    

        fornecedor_window = sg.Window("Cadastro de Fornecedores", fornecedor_layout, size=(400,500))

         #While da janela de  cadastro de fornecedores
        while True:
            event, values = fornecedor_window.read()
     
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                fornecedor_window.close()
                break


            #interagindo com o banco esalvando os dados
            c.execute("INSERT INTO fornecedor (nome, cnpj, endereco, telefone, cidade, estado) VALUES (?, ?, ?, ?, ?, ?)", (values["nome"], values["cnpj"],values["endereco"],values["telefone"],values["cidade"],values["estado"]))
            conn.commit()

            #Limpar iputs após o cadastro
            fornecedor_window["nome"].update("")
            fornecedor_window["cnpj"].update("")
            fornecedor_window["endereco"].update("")
            fornecedor_window["telefone"].update("")
            fornecedor_window["cidade"].update("")
            fornecedor_window["estado"].update("")

            #Confirmar o cadastro
            sg.popup("Fornecedor Cadastrado com sucesso!", title="Cadastro")

        fornecedor_window.close()





    elif event == "Cadastro Transportadoras":

        #criar layout da seguna tela que aparece quando clica em cadastrar Transportadora
        transp_layout = [
            [sg.Text("Nome")],      
            [sg.InputText(key="nome")],
            [sg.Text("CNPJ")],      
            [sg.InputText(key="cnpj")],
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
    

        transp_window = sg.Window("Cadastro de Transportadoras", transp_layout, size=(400,500))

         #While da janela de  cadastro de fornecedores
        while True:
            event, values = transp_window.read()
     
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                transp_window.close()
                break


            #interagindo com o banco esalvando os dados
            c.execute("INSERT INTO transport (nome, cnpj, endereco, telefone, cidade, estado) VALUES (?, ?, ?, ?, ?, ?)", (values["nome"], values["cnpj"],values["endereco"],values["telefone"],values["cidade"],values["estado"]))
            conn.commit()

            #Limpar iputs após o cadastro
            transp_window["nome"].update("")
            transp_window["cnpj"].update("")
            transp_window["endereco"].update("")
            transp_window["telefone"].update("")
            transp_window["cidade"].update("")
            transp_window["estado"].update("")



        
        transp_window.close() 

            
    if event == "Consulta Clientes":
    
            consulta_layout =[
                [sg.Text("Clientes")],
                [sg.InputText(key="clientes")],
                [sg.Button("Consultar")],
                [sg.Button("Cancelar")],
                [sg.Table(values=[], headings=["nome","cpf","endereco","telefone","cidade","estado"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")]
            ]    
            consulta_window = sg.Window("Consulta de Clientes", consulta_layout, resizable=True)

        #loop eventos
        
            while True:
                event, values = consulta_window.read()
            
                if event == sg.WIN_CLOSED or event == "Cancelar":
                    consulta_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["clientes"].upper()
                c.execute( "SELECT nome, cpf, endereco,telefone,cidade,estado FROM clientes WHERE UPPER(nome) = ?",(produto_busca,))
                registros = c.fetchall()

                # ATUALIZAR
                tabela = consulta_window["tabela"]
                tabela.update(values=registros) # ATUALIZA A TELA COM OS DADOS QUE ESTAVA ARMAZENADO NA VARIÁVEL "registros"    
                       
            consulta_window.close()  
    
            
    elif event == "Consulta Fornecedores":
    
            consulta_layout =[
                [sg.Text("Consultar_Fornecedor")],
                [sg.InputText(key="fornecedor")],
                [sg.Button("Consultar")],
                [sg.Button("Cancelar")],
                [sg.Table(values=[], headings=["nome","cnpj","endereco","telefone","cidade","estado"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")]
            ]    
            consulta_window = sg.Window("Consulta de Fornecedores", consulta_layout, resizable=True)

        #loop eventos
        
            while True:
                event, values = consulta_window.read()
            
                if event == sg.WIN_CLOSED or event == "Cancelar":
                    consulta_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["fornecedor"].upper()
                c.execute( "SELECT nome, cnpj, endereco,telefone,cidade,estado FROM fornecedor WHERE UPPER(nome) = ?",(produto_busca,))
                registros = c.fetchall()

                # ATUALIZAR
                tabela = consulta_window["tabela"]
                tabela.update(values=registros)     
                       
            consulta_window.close()  


    # AQUI ENTRAMOS NO MENU DE CONSULTA DAS TRANSPORTADORAS CADASTRADAS        
    elif event == "Consulta Transportadoras":
    
            consulta_layout =[
                [sg.Text("Consultar Transportadora")],
                [sg.InputText(key="transportadora")],
                [sg.Button("Consultar")],
                [sg.Button("Cancelar")],
                [sg.Table(values=[], headings=["nome","cnpj","endereco","telefone","cidade","estado"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")]
            ]    
            consulta_window = sg.Window("Consulta de Transportadora", consulta_layout, resizable=True)

        #loop eventos
        
            while True:
                event, values = consulta_window.read()
            
                if event == sg.WIN_CLOSED or event == "Cancelar":
                    consulta_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["transportadora"].upper()
                c.execute( "SELECT nome, cnpj, endereco,telefone,cidade,estado FROM transport WHERE UPPER(nome) = ?",(produto_busca,))
                registros = c.fetchall()

                # ATUALIZAR
                tabela = consulta_window["tabela"]
                tabela.update(values=registros)     
                       
            consulta_window.close()
            
            
            
            
            
            
            
            
            
                                # -----------RELATÓRIOS------------ #       
    elif event == "Relatório Fornecedores": 
    
            relatorio_layout =[
                [sg.Text("Relatório Fornecedores")],
                [sg.InputText(key="fornecedor")],
                [sg.Button("Gerar Relatório")],
                [sg.Button("Cancelar")]
                
            ]    
            relatorio_window = sg.Window("Relatório de Fornecedores", relatorio_layout, resizable=True)

        #loop eventos
        
            while True:
                event, values = relatorio_window.read()
            
                if event == sg.WIN_CLOSED or event == "Cancelar":
                    relatorio_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["fornecedor"].upper()
                c.execute( "SELECT * FROM fornecedor WHERE UPPER(nome) = ?",(produto_busca,))
                registro = c.fetchone()
                
                if registro:
                    with open("C:/Users/patri/OneDrive/Área de Trabalho/DataBase/Relatório_Fornecedores.html","w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório<h1><table border='1'><tr><th>Nome</th><th>Cnpj</th><th>Endereço</th><th>Telefone</th><th>Cidade</th><th>Estado</th></tr>")
                        f.write(f"<tr><th>{registro[0]}</th><th>{registro[1]}</th><th>{registro[2]}</th><th>{registro[3]}</th><th>{registro[4]}</th><th>{registro[5]}</th></tr>")
                        f.write("</body></html>")
                    
                        sg.popup("Relatório Gerado com Sucesso!!", title="Relatório") # MENSAGEM QUE APARECE APÓS GERAR O RELATÓRIO
                
                else :
                    sg.popup("Fornecedor não Encontrado no Sistema!!", title="Relatório")
                

                    # ATUALIZAR OS DADOS DA PESQUISA APÓS REAKIZADA COM SUCESSO
                    relatorio_window["fornecedor"].update ("")
                    relatorio_window.update (values="registro")     
                       
                relatorio_window.close()    # DEVE FICAR NA LINHA DO BREAK PARA FECHAR A TELA APÓS O POPUP
            
            
          # RELATÓRIO DE TRANPORTADORAS  
    elif event == "Relatório Transportadoras": 
    
            relatorio_layout =[
                [sg.Text("Relatório Transportadoras")],
                [sg.InputText(key="transport")],
                [sg.Button("Gerar Relatório")],
                [sg.Button("Cancelar")]
                
            ]    
            relatorio_window = sg.Window("Relatório de Transportadoras", relatorio_layout, resizable=True)

        #loop eventos
        
            while True:
                event, values = relatorio_window.read()
            
                if event == sg.WIN_CLOSED or event == "Cancelar":
                    relatorio_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["transport"].upper() # upper DEIXA A PESQUISA PADRÂO NO BANCO DE DADOS PARA NÂO HAVER ERRO NA QUERY
                c.execute( "SELECT * FROM transport WHERE UPPER(nome) = ?",(produto_busca,))
                registro = c.fetchone()
                
                if registro:
                    with open("C:/Users/patri/OneDrive/Área de Trabalho/DataBase/Relatório_transportadoras.html","w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório<h1><table border='1'><tr><th>Nome</th><th>Cnpj</th><th>Endereço</th><th>Telefone</th><th>Cidade</th><th>Estado</th></tr>")
                        f.write(f"<tr><th>{registro[0]}</th><th>{registro[1]}</th><th>{registro[2]}</th><th>{registro[3]}</th><th>{registro[4]}</th><th>{registro[5]}</th></tr>")
                        f.write("</body></html>")
                    
                        sg.popup("Relatório Gerado com Sucesso!!", title="Relatório") # MENSAGEM QUE APARECE APÓS GERAR O RELATÓRIO
                
                else :
                    sg.popup("Transportadora não Encontrado no Sistema!!", title="Relatório")
                

                    # ATUALIZAR OS DADOS DA PESQUISA APÓS REAKIZADA COM SUCESSO
                    relatorio_window["transport"].update ("")
                    relatorio_window.update (values="registro")     
                       
                relatorio_window.close()    # DEVE FICAR NA LINHA DO BREAK PARA FECHAR A TELA APÓS O POPUP        
            


   # RELATÓRIO DE CLIENTES         
    elif event == "Relatório Clientes": 
    
            relatorio_layout =[
                [sg.Text("Relatório Clientes")],
                [sg.InputText(key="clientes")],
                [sg.Button("Gerar Relatório")],
                [sg.Button("Cancelar")]
                
            ]    
            relatorio_window = sg.Window("Relatório de Clientes", relatorio_layout, resizable=True)

        #loop eventos
        
            while True:
                event, values = relatorio_window.read()
            
                if event == sg.WIN_CLOSED or event == "Cancelar":
                    relatorio_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["clientes"].upper() # upper DEIXA A PESQUISA PADRÂO NO BANCO DE DADOS PARA NÂO HAVER ERRO NA QUERY
                c.execute( "SELECT * FROM clientes WHERE UPPER(nome) = ?",(produto_busca,))
                registro = c.fetchone()
                
                if registro:
                    with open("C:/Users/patri/OneDrive/Área de Trabalho/DataBase/Relatório_Clientes.html","w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório<h1><table border='1'><tr><th>Nome</th><th>cpf</th><th>Endereço</th><th>Telefone</th><th>Cidade</th><th>Estado</th></tr>")
                        f.write(f"<tr><th>{registro[0]}</th><th>{registro[1]}</th><th>{registro[2]}</th><th>{registro[3]}</th><th>{registro[4]}</th><th>{registro[5]}</th></tr>")
                        f.write("</body></html>")
                    
                        sg.popup("Relatório Gerado com Sucesso!!", title="Relatório") # MENSAGEM QUE APARECE APÓS GERAR O RELATÓRIO
                
                else :
                    sg.popup("Cliente não Encontrado no Sistema!!", title="Relatório")
                

                    # ATUALIZAR OS DADOS DA PESQUISA APÓS REAKIZADA COM SUCESSO
                    relatorio_window["clientes"].update ("")
                    relatorio_window.update (values="registro")     
                       
                relatorio_window.close()    # DEVE FICAR NA LINHA DO BREAK PARA FECHAR A TELA APÓS O POPUP         
            
            
            


window.close()

conn.close()       
     
     
     
  
