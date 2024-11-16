from tkinter import Tk, Canvas, Button, PhotoImage

def carregar_dados_usuario(nome, email, nivel_acesso):
    window = Tk()
    window.geometry("1000x700")
    window.configure(bg="#E6F4EA")
    window.iconbitmap('fingerprint.ico')
    window.title(f"Perfil de {nome}")
    window.resizable(False, False)

    # Centraliza a janela
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (1000 // 2)
    y = (screen_height // 2) - (700 // 2)
    window.geometry(f"1000x700+{x}+{y}")

    canvas = Canvas(window, bg="#E6F4EA", height=700, width=1000, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    # Cabeçalho
    canvas.create_rectangle(0, 0, 1000, 80, fill="#32a852", outline="")
    canvas.create_text(500, 40, text=f"Bem-vindo, {nome}!", fill="#FFFFFF", font=("Roboto Bold", 24))

    # Título de Perfil
    canvas.create_text(500, 200, text="Perfil do Usuário", fill="#32a852", font=("Roboto Bold", 36))

    # Textos
    canvas.create_text(310, 300, text=f"Nome:", fill="#32a852", font=("Roboto Bold", 20), anchor="e")
    canvas.create_text(330, 300, text=nome, fill="#000716", font=("Roboto", 20), anchor="w")

    canvas.create_text(310, 350, text=f"E-mail:", fill="#32a852", font=("Roboto Bold", 20), anchor="e")
    canvas.create_text(330, 350, text=email, fill="#000716", font=("Roboto", 20), anchor="w")

    canvas.create_text(430, 400, text=f"Nível de Acesso:", fill="#32a852", font=("Roboto Bold", 20), anchor="e")
    canvas.create_text(450, 400, text=nivel_acesso, fill="#000716", font=("Roboto", 20), anchor="w")

    def voltar():
        window.destroy()
        import login 

    seta_imagem = PhotoImage(file="goback.png").subsample(9, 9)
    button_voltar = Button(
        window,
        image=seta_imagem,
        bg="#FFFFFF",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=voltar,
        cursor="hand2"
    )
    button_voltar.place(x=10, y=10)
    button_voltar.image = seta_imagem

    window.mainloop()