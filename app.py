import customtkinter as ctk
from PIL import Image
import oracledb

#configuração da aparência
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


#configurando variavel da imagem

image_background = Image.open("./media/fundo.png")

background_ctkimage = ctk.CTkImage(light_image=image_background, dark_image=image_background, size=(800,500))

query = input(str("Digite a sua query: "))


class DatabaseFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill='both', expand=True)
        label = ctk.CTkLabel(self, text='Bem vindo a página de banco de dados')
        label.pack(pady=20)
        
    def rundba(self):

        try:

            wallet = 'wallet'
            
            service_name = 'v268zgxpbu2loi9n_high'

            connection = oracledb.connect(
                user = 'WKSP_PROJETOINTEGRADOR',
                password =  'Azulamarelo123quatro-',
                dsn = service_name,
                config_dir = wallet,
                wallet_location = wallet,
                wallet_password = 'Azulamarelo1234cinco-'
                
            )
            
            cursor = connection.cursor()
            resultado = cursor.execute(query)


            linhas = cursor.fetchall()[0]
            count_linhas = len(linhas)

            colunas = cursor.description
            colunas_nome  = []
            count_colunas = 0
                        
            frame_colunas = ctk.CTkFrame(self, border_color='#7C7C7C', border_width=2, fg_color='transparent')
            frame_colunas.place(relx=0, rely=0, relwidth=1, relheight=0.1)  # topo (10% da tela)

            frame_linha_valor = ctk.CTkFrame(self, border_color='#7C7C7C', border_width=2, fg_color='transparent')
            frame_linha_valor.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)  # abaixo (90%)

            
            for coluna in colunas:
                colunas_nome.append(coluna[0])
            
            count_colunas = len(colunas_nome)


            
            # for coluna_nome in colunas:
            #     label = ctk.CTkLabel(frame_colunas, text=f"{coluna_nome[0]}", fg_color='transparent', width=130, text_color='black')
            #     label.grid(row=0, column=count_linhas, padx=10, pady=10)
                
            
        
            for coluna_nome in range(count_colunas):
                label = ctk.CTkLabel(frame_colunas, text=f"{colunas_nome[coluna_nome]}", fg_color='white', width=130, text_color='black')
                label.grid(row=0, column=coluna_nome, padx=10, pady=10)
            
            
            for linha_valor in range(count_linhas):
                label = ctk.CTkLabel(frame_linha_valor, text=f"{linhas[linha_valor]}",fg_color="#7C7C7C", width=130, text_color='black')
                label.grid(row=0, column=linha_valor, padx=10, pady=10)
            

            connection.close()
            
        except Exception as e:
            print(e)
        
        


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema DOC IO")
        self.geometry("1050x500")
        
        self.background_img()
        self.sidebar()
    
    def background_img(self):
        frame_background = ctk.CTkLabel(self, image=background_ctkimage, text='')
        frame_background.pack(side='right', fill='both')
        
    def sidebar(self):
        
        def validar_login():
            usuario = campo_usuario.get()
            senha = campo_senha.get()
            
            if usuario != 'leonardo' or senha != '123':
                resultado_login.configure(text="Erro no login, verifique seus dados !", text_color="red")
                
            else:
                resultado_login.configure(text="Login feito com sucesso !", text_color="green")
                self.show_database()
        
        sidebar = ctk.CTkFrame(self, fg_color="transparent")
        sidebar.place(relx=0, rely=0, relwidth=0.25, relheight=1)


        #frame dentro do sidebar
        container_insidebar = ctk.CTkFrame(sidebar, fg_color='transparent')
        container_insidebar.place(relx = 0, rely=0, relwidth=1, relheight=1)
        
        #Crescimento para cada linha
        container_insidebar.grid_rowconfigure(0, weight=1)
        container_insidebar.grid_rowconfigure(1, weight=1)
        container_insidebar.grid_rowconfigure(2, weight=1)
        container_insidebar.grid_rowconfigure(3, weight=1)
        container_insidebar.grid_rowconfigure(4, weight=1)
        container_insidebar.grid_rowconfigure(5, weight=1)
        container_insidebar.grid_columnconfigure(0, weight=1)



        #Label1
        label_usuario = ctk.CTkLabel(container_insidebar,text="Usuário")
        label_usuario.grid(row = 0, column = 0, sticky='nsew')

        # #Entry1
        campo_usuario = ctk.CTkEntry(container_insidebar, placeholder_text="Digite seu usuário")
        campo_usuario.grid(row = 1, column = 0, sticky='nsew')

        # #Label2
        label_senha = ctk.CTkLabel(container_insidebar,text="Senha")
        label_senha.grid(row = 2, column = 0, sticky='nsew')

        # #Entry3
        campo_senha = ctk.CTkEntry(container_insidebar, placeholder_text="Digite sua senha")
        campo_senha.grid(row = 3, column = 0, sticky='nsew')



        # #Button
        botao_login = ctk.CTkButton(container_insidebar,text="Login", command=validar_login)
        botao_login.grid(row = 4, column = 0, sticky='nsew')

        # #campo feedback login
        resultado_login = ctk.CTkLabel(container_insidebar, text='')
        resultado_login.grid(row = 5, column = 0, sticky='nsew')
    
    def clear_widget(self):
        for widget in self.winfo_children():
            widget.destroy()
        
    
        
    def show_database(self):
        self.clear_widget()
        DatabaseFrame(self)
        DatabaseFrame.rundba(self)        
        


        
        

app = MainWindow()
app.mainloop()

        





#criação das funções de funcionalidades, antes da janela gráfica

# def validar_login():
#     usuario = campo_usuario.get()
#     senha = campo_senha.get()
    
#     if usuario != 'leonardo' or senha != '123':
#         resultado_login.configure(text="Erro no login, verifique seus dados !", text_color="red")
#     else:
#         resultado_login.configure(text="Login feito com sucesso !", text_color="green")
    




# #criação da janela principal 
# main_window = ctk.CTk()
# main_window.title("Sistema de Login")
# main_window.geometry("1050x500")


# #criacao do frame principal

# frame_background = ctk.CTkLabel(main_window, image=background_ctkimage, text='')
# frame_background.pack(side='right', fill='both')


# #criação do sidebar

# sidebar = ctk.CTkFrame(main_window, fg_color="transparent")
# sidebar.place(relx=0, rely=0, relwidth=0.25, relheight=1)


# #criação dos campos

# #Label1
# label_usuario = ctk.CTkLabel(sidebar,text="Usuário")
# label_usuario.pack(pady=10)

# #Entry1
# campo_usuario = ctk.CTkEntry(sidebar, placeholder_text="Digite seu usuário")
# campo_usuario.pack(pady=10)

# #Label2
# label_senha = ctk.CTkLabel(sidebar,text="Senha")
# label_senha.pack(pady=10)

# #Entry3
# campo_senha = ctk.CTkEntry(sidebar, placeholder_text="Digite sua senha")
# campo_senha.pack(pady=10)



# #Button
# botao_login = ctk.CTkButton(sidebar,text="Login", command=validar_login)
# botao_login.pack(pady=10)

# #campo feedback login
# resultado_login = ctk.CTkLabel(sidebar, text='')
# resultado_login.pack(pady=10)







# #Iniciar aplicação
# main_window.mainloop()