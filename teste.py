import customtkinter as ctk

# Inicializa o modo escuro (pode ser "System", "Light", "Dark")
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")  # Você pode usar: "blue", "green", "dark-blue"

# Cria a janela principal
app = ctk.CTk()
app.geometry("800x500")
app.title("Interface com Sidebar")

# Cria a sidebar (frame lateral)
sidebar = ctk.CTkFrame(app, width=200, corner_radius=20, fg_color='red')
sidebar.pack(side="left", fill="y")

# Adiciona alguns botões à sidebar
btn1 = ctk.CTkButton(sidebar, text="Página 1")
btn1.pack(pady=10, padx=20)

btn2 = ctk.CTkButton(sidebar, text="Página 2")
btn2.pack(pady=10, padx=20)

btn3 = ctk.CTkButton(sidebar, text="Sair", command=app.quit)
btn3.pack(pady=10, padx=20)

# Cria o conteúdo principal
main_content = ctk.CTkFrame(app)
main_content.pack(side="right", fill="both", expand=True)

label = ctk.CTkLabel(main_content, text="Conteúdo principal aqui", font=ctk.CTkFont(size=18))
label.pack(pady=20)

# Roda o app
app.mainloop()
