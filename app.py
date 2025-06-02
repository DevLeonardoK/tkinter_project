import customtkinter as ctk
from PIL import Image

#configuração da aparência
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


#configurando variavel da imagem

image_background = Image.open("./media/fundo.png")

background_ctkimage = ctk.CTkImage(light_image=image_background, dark_image=image_background, size=(800,500))

#criação das funções de funcionalidades, antes da janela gráfica

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    if usuario != 'leonardo' or senha != '123':
        resultado_login.configure(text="Erro no login, verifique seus dados !", text_color="red")
    else:
        resultado_login.configure(text="Login feito com sucesso !", text_color="green")
    




#criação da janela principal 
main_window = ctk.CTk()
main_window.title("Sistema de Login")
main_window.geometry("1050x500")


#criacao do frame principal

frame_background = ctk.CTkLabel(main_window, image=background_ctkimage, text='')
frame_background.pack(side='right', fill='both')


#criação do sidebar

sidebar = ctk.CTkFrame(main_window, fg_color="transparent")
sidebar.place(relx=0, rely=0, relwidth=0.25, relheight=1)


#criação dos campos

#Label1
label_usuario = ctk.CTkLabel(sidebar,text="Usuário")
label_usuario.pack(pady=10)

#Entry1
campo_usuario = ctk.CTkEntry(sidebar, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=10)

#Label2
label_senha = ctk.CTkLabel(sidebar,text="Senha")
label_senha.pack(pady=10)

#Entry3
campo_senha = ctk.CTkEntry(sidebar, placeholder_text="Digite sua senha")
campo_senha.pack(pady=10)



#Button
botao_login = ctk.CTkButton(sidebar,text="Login", command=validar_login)
botao_login.pack(pady=10)

#campo feedback login
resultado_login = ctk.CTkLabel(sidebar, text='')
resultado_login.pack(pady=10)







#Iniciar aplicação
main_window.mainloop()