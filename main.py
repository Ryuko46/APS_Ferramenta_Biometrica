from tkinter import Tk, Canvas, Button, PhotoImage

# Funções de Navegação
def abrir_tela_login():
    window.destroy()
    import login  # Abre a tela de login

def abrir_tela_cadastro():
    window.destroy()
    import cadastro  # Abre a tela de cadastro

# Funções de Animação de Botões
def on_enter(event):
    event.widget['bg'] = '#279645'

def on_leave(event):
    event.widget['bg'] = '#32a852'

# Configuração da Janela Principal
window = Tk()
window.geometry("1000x700")
window.configure(bg="#E6F4EA")  # Fundo verde claro
window.iconbitmap('fingerprint.ico')
window.title('Bem-vindo')
window.resizable(False, False)

# Centraliza a janela
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (1000 // 2)
y = (screen_height // 2) - (700 // 2)
window.geometry(f"1000x700+{x}+{y}")

# Configuração do Canvas
canvas = Canvas(window, bg="#E6F4EA", height=700, width=1000, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# Cabeçalho com Título e Ícone
canvas.create_rectangle(0, 0, 1000, 80, fill="#32a852", outline="")
brasil_image = PhotoImage(file="brasil.png").subsample(20, 20)
canvas.create_image(50, 40, image=brasil_image, anchor="center")
canvas.create_text(500, 40, text="Ministério do Meio Ambiente", fill="#FFFFFF", font=("Roboto Bold", 24))

# Mensagem de Boas-vindas
canvas.create_text(500, 200, text="Bem-vindo!", fill="#32a852", font=("Roboto Bold", 36))
canvas.create_text(500, 270, text="Escolha uma opção abaixo para continuar:", fill="#000716", font=("Roboto", 20))

# Botão "Fazer Login"
button_login = Button(
    text="Fazer Login",
    font=("Roboto Bold", 18),
    bg="#32a852",
    fg="#FFFFFF",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    cursor="hand2",
    command=abrir_tela_login
)
button_login.place(x=400, y=370, width=200, height=60)
button_login.bind("<Enter>", on_enter)
button_login.bind("<Leave>", on_leave)

# Botão "Cadastrar-se"
button_cadastro = Button(
    text="Cadastrar-se",
    font=("Roboto Bold", 18),
    bg="#32a852",
    fg="#FFFFFF",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    cursor="hand2",
    command=abrir_tela_cadastro
)
button_cadastro.place(x=400, y=470, width=200, height=60)
button_cadastro.bind("<Enter>", on_enter)
button_cadastro.bind("<Leave>", on_leave)

# Inicia a Aplicação
window.mainloop()
