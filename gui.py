import cv2
import fingerprint_feature_extractor
import re

from pathlib import Path
from tkinter import Tk, ttk, Canvas, Text, Entry, OptionMenu, StringVar, Button, filedialog, IntVar, Radiobutton, messagebox, Label,PhotoImage
from banco import cadastrar_usuario  # Importando a função de cadastro do banco de dados


documento_selecionado = None  # Variável global para armazenar o caminho da imagem

def selecionar_documento():
    global documento_selecionado
    documento_selecionado = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png;*.jpg;*.tif;*.jpeg;*.gif")]
    )
    # Atualiza o label com o nome da imagem selecionada

def preprocess_image(documento_selecionado):
    global image1 
    image1 = cv2.imread(documento_selecionado, cv2.IMREAD_GRAYSCALE)
    if image1 is None:
        raise ValueError(f"Image not found at {documento_selecionado}")
    return image1

def extract_features(image1):
    # Extrai as características de minutiae
    FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(image1)
    return FeaturesTerminations + FeaturesBifurcations

def clean_features(features):
    # Extrai apenas o endereço hexadecimal e converte para inteiro
    return [int(re.search(r'0x[0-9A-Fa-f]+', str(item)).group(), 16) for item in features]

def cadastrar():
    nome = entry_1.get().strip()
    email = entry_2.get().strip()
    
    # Extrai o número do nível de acesso (ex.: "Nível 1" -> "1")
    nivel_acesso_str = nivel_var.get()
    nivel_acesso = nivel_acesso_str.split()[-1]  # Pega o último elemento da string ("1", "2" ou "3")
    
    # Verifica se todos os campos foram preenchidos
    if not nome or not email or not documento_selecionado:
        messagebox.showwarning("Campos Incompletos", "Por favor, preencha todos os campos antes de cadastrar.")
        return

    # Processa a primeira imagem
    imagecad = preprocess_image(documento_selecionado)
    features1 = extract_features(imagecad)
    global features1_clean
    features1_clean = clean_features(features1)
    sucesso, mensagem = cadastrar_usuario(nome, email, int(nivel_acesso), features1_clean)
    
    if sucesso:
        messagebox.showinfo("Cadastro Realizado", "Os dados foram cadastrados com sucesso!")
    else:
        messagebox.showerror("Erro no Cadastro", f"Ocorreu um erro ao cadastrar os dados: {mensagem}")


def abrir_tela_login():
    window.destroy()  # Fecha a tela de cadastro
    import login  # Importa e abre a tela de login

window = Tk()

window_width = 1000
window_height = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg="#FFFFFF")
window.iconbitmap('fingerprint.ico')
window.title('Cadastro - Ministério do Meio Ambiente')

canvas = Canvas(
    window,
    bg="#E6F4EA",
    height=700,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

# Carregar a imagem da seta
seta_imagem = PhotoImage(file="goback.png")

# Redimensionar a imagem (ajustar o fator conforme necessário)
seta_imagem = seta_imagem.subsample(9, 9)  # Reduz 5 vezes em largura e altura

# Função para voltar à tela inicial
def voltar_tela_inicial():
    window.destroy()  # Esconde a janela de cadastro ou login
    import main  # Exibe a tela inicial

# Botão de "Voltar"
button_voltar = Button(
    window, 
    image=seta_imagem, 
    bg="#FFFFFF", 
    borderwidth=0, 
    highlightthickness=0, 
    relief="flat", 
    command=voltar_tela_inicial, 
    cursor="hand2"
)
button_voltar.place(x=10, y=10)  # Posição no canto superior esquerdo

# Manter a referência da imagem para evitar que seja coletada como lixo
button_voltar.image = seta_imagem

canvas.place(x=0, y=0)

# Fundo roxo do lado esquerdo
canvas.create_rectangle(0.0, 0.0, 500.0, 700.0, fill="#32a852", outline="")

# Títulos e textos informativos
canvas.create_text(59.0, 96.0, anchor="nw", text="Bem Vindo", fill="#FFFFFF", font=("Roboto Bold", 32))
canvas.create_rectangle(59.0, 160.0, 155.0, 147.0, fill="#FFFFFF", outline="")

canvas.create_text(
    59.0, 217.0, anchor="nw",
    text="Acesso ao Banco de Dados do Ministério\ndo Meio Ambiente.",
    fill="#FFFFFF", font=("Roboto Bold", 16)
)

canvas.create_text(
    59.0, 309.0, anchor="nw",
    text="Por favor insira as informações solicitadas\npara que a sua conta possa ser cadastrada\nem nosso sistema.",
    fill="#FFFFFF", font=("Roboto Bold", 16)
)

canvas.create_text(553.0, 85.0, anchor="nw", text="Cadastro.", fill="#32a852", font=("Roboto Bold", 32))

# Labels dos campos
canvas.create_text(553.0, 176.0, anchor="nw", text="Nome", fill="#32a852", font=("Roboto Bold", 18))
canvas.create_text(553.0, 265.0, anchor="nw", text="Email", fill="#32a852", font=("Roboto Bold", 18))
canvas.create_text(553.0, 362.0, anchor="nw", text="Nível de Acesso", fill="#32a852", font=("Roboto Bold", 18))

# Campos de entrada estilizados
entry_1 = Entry(bd=0, bg="#ffffff", fg="#000716", font=("Roboto", 16), highlightthickness=1, highlightbackground="#32a852")
entry_1.place(x=560.0, y=204.0, width=367.0, height=42.0)

entry_2 = Entry(bd=0, bg="#ffffff", fg="#000716", font=("Roboto", 16), highlightthickness=1, highlightbackground="#32a852")
entry_2.place(x=560.0, y=293.0, width=367.0, height=42.0)

## Variável para o nível de acesso e configuração do estilo personalizado
nivel_var = StringVar()
nivel_var.set("Selecione")  # Inicializa vazio para forçar o usuário a escolher

# Estilo personalizado para o OptionMenu
style = ttk.Style()
style.configure("TMenubutton", font=("Roboto", 14), background="#ffffff", foreground="#000716", relief="flat")
style.map("TMenubutton", background=[("active", "#C8E4CB")])  # Cor quando o botão estiver ativo

# Menu de seleção para o nível de acesso com estilo
nivel_opcoes = ["Nível 1", "Nível 2", "Nível 3"]
option_menu_nivel = ttk.OptionMenu(window, nivel_var, "", *nivel_opcoes)
option_menu_nivel.place(x=560.0, y=390.0, width=150, height=40)

# Label para mostrar o nome da imagem selecionada
label_nome_imagem = Label(window, text="", bg="#E6F4EA", fg="#32a852", font=("Roboto", 14))
label_nome_imagem.place(x=636.0, y=505.0)

# Botão "Impressão Digital"
button_1 = Button(
    text="Impressão Digital",
    font=("Roboto Bold", 16),
    bg="#32a852",
    fg="#FFFFFF",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=selecionar_documento, 
    cursor="hand2"
)
button_1.place(x=636.0, y=535.0, width=215.0, height=46.0)

# Botão "CADASTRAR"
button_2 = Button(
    text="CADASTRAR",
    font=("Roboto Bold", 16),
    bg="#32a852",
    fg="#FFFFFF",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=cadastrar, 
    cursor="hand2"
)
button_2.place(x=650.0, y=607.0, width=188.0, height=56.0)

def sublinhar(event):
    label_login.config(font=("Roboto", 14, "underline"))  # Adiciona o sublinhado ao passar o mouse

# Função para remover o sublinhado quando o mouse sair
def remover_sublinhado(event):
    label_login.config(font=("Roboto", 14))  # Restaura o estilo original

label_login = Label(window, text="Já tenho uma conta", fg="#32a852", bg="#E6F4EA", font=("Roboto", 14), cursor="hand2")
label_login.place(x=656.0, y=670.0)
label_login.bind("<Enter>", sublinhar)  # Ao passar o mouse
label_login.bind("<Leave>", remover_sublinhado)  # Ao sair do mouse
label_login.bind("<Button-1>", lambda e: abrir_tela_login())



def on_enter(event):
    event.widget['bg'] = '#4BCF6B' 

def on_leave(event):
    event.widget['bg'] = '#32a852'

button_1.bind("<Enter>", on_enter)
button_1.bind("<Leave>", on_leave)
button_2.bind("<Enter>", on_enter)
button_2.bind("<Leave>", on_leave)

window.resizable(False, False)
window.mainloop()
