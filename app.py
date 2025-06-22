import customtkinter as ctk
from PIL import Image

#configuração da aparência
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


#configurando variavel da imagem

image_background = Image.open("./media/fundo.png")

background_ctkimage = ctk.CTkImage(light_image=image_background, dark_image=image_background, size=(800,500))


class DatabaseFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill='both', expand=True)
        label = ctk.CTkLabel(self, text='Bem vindo a página de banco de dados')
        label.pack(pady=20)


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