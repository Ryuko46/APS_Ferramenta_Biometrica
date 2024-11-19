import cv2
import fingerprint_feature_extractor
import re

from pathlib import Path
from tkinter import Tk, Canvas, Button, Label, filedialog, messagebox, PhotoImage, Frame
from banco import comparador
from telasucesso import carregar_dados_usuario

documento_selecionado2 = None  # Variável global para armazenar o caminho da imagem

def selecionar_documento():
    global documento_selecionado2
    documento_selecionado2 = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png;*.jpg;*.tif;*.jpeg;*.gif")]
    )
    if documento_selecionado2:
        nome_imagem = Path(documento_selecionado2).name
        label_nome_imagem.config(text=nome_imagem)

def preprocessa_imagem(documento_selecionado2):
    global image2 
    image2 = cv2.imread(documento_selecionado2, cv2.IMREAD_GRAYSCALE)
    if image2 is None:
        raise ValueError(f"Image not found at {documento_selecionado2}")
    return image2

def extracao_features(image2):
    # Extrai as características de minutiae
    FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(image2, invertImage=True)
    return FeaturesTerminations + FeaturesBifurcations

def limpar_features(features):
    # Extrai apenas o endereço hexadecimal e converte para inteiro
    return [int(re.search(r'0x[0-9A-Fa-f]+', str(item)).group(), 16) for item in features]

def login():
    if not documento_selecionado2:
        messagebox.showwarning("Erro", "Por favor, selecione uma imagem de impressão digital.")
        return
   
    #Processa segunda imagem e retorna
    imagelog = preprocessa_imagem(documento_selecionado2)
    features2 = extracao_features(imagelog)
    global features2_clean
    features2_clean = limpar_features(features2)

    # Realiza a busca no banco de dados pelo nome da imagem
    dados_usuario, resultado = comparador(features2_clean)    
    
    if dados_usuario:
        nome_usuario, email, nivel_acesso = dados_usuario
        window.destroy()  # Fecha a tela de login
        carregar_dados_usuario(nome_usuario, email, nivel_acesso)
    else:
        messagebox.showerror("Erro no Login", resultado)

def abrir_tela_cadastro():
    window.destroy()  # Fecha a tela de login
    import cadastro  # Importa e abre a tela de cadastro

# Configuração da janela principal
window = Tk()
window_width = 1000
window_height = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg="#F8F8FF")
window.iconbitmap('images/fingerprint.ico')
window.title('Login - Ministério do Meio Ambiente')

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
seta_imagem = PhotoImage(file="images/goback.png")

# Redimensionar a imagem (ajustar o fator conforme necessário)
seta_imagem = seta_imagem.subsample(9, 9)  # Reduz 5 vezes em largura e altura

# Função para voltar à tela inicial
def voltar_tela_inicial():
    window.destroy()  # Esconde a janela de cadastro ou login
    import main
  # Exibe a tela inicial

def importar_main():
    window_main = Tk()
    window_main.title("Tela Inicial")
    
    # Adiciona botões para cadastro e login
    button_cadastrar = Button(window_main, text="Cadastrar", command=abrir_tela_cadastro)
    button_cadastrar.pack()
    
    button_login = Button(window_main, text="Fazer Login", command=login)
    button_login.pack()

    window_main.mainloop()


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

# Fundo verde do lado direito
canvas.create_rectangle(500.0, 0.0, 1000.0, 700.0, fill="#32a852", outline="")

# Títulos e textos informativos agora à direita
canvas.create_text(553.0, 96.0, anchor="nw", text="Bem Vindo", fill="#E6F4EA", font=("Roboto Bold", 32))
canvas.create_rectangle(553.0, 160.0, 649.0, 147.0, fill="#E6F4EA", outline="")

canvas.create_text(
    553.0, 217.0, anchor="nw",
    text="Acesso ao Banco de Dados do Ministério\ndo Meio Ambiente.",
    fill="#FFFFFF", font=("Roboto Bold", 16)
)

canvas.create_text(
    553.0, 309.0, anchor="nw",
    text="Por favor insira as informações solicitadas\npara que você possa acessar a sua\nconta no nosso sistema.",
    fill="#FFFFFF", font=("Roboto Bold", 16)
)

canvas.create_text(60.0, 96.0, anchor="nw", text="Login", fill="#32a852", font=("Roboto Bold", 32))


# Centralizando os elementos na metade esquerda
label_impressao = canvas.create_text(250.0, 200.0, anchor="center", text="Impressão Digital", fill="#32a852", font=("Roboto Bold", 18))

# Label para exibir o nome da imagem selecionada
label_nome_imagem = Label(window, text="", bg="#F8F8FF", fg="#000716", font=("Roboto", 14))
label_nome_imagem.place(x=175.0, y=320.0)

# Botão "Selecionar Impressão Digital" centralizado
button_1 = Button(
    text="Selecionar",
    font=("Roboto Bold", 16),
    bg="#32a852",
    fg="#FFFFFF",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=selecionar_documento, 
    cursor="hand2"
)
button_1.place(x=175.0, y=250.0, width=150.0, height=46.0)  # Posição centralizada

# Botão "LOGIN"
button_2 = Button(
    text="LOGIN",
    font=("Roboto Bold", 16),
    bg="#32a852",
    fg="#FFFFFF",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=login, 
    cursor="hand2"
)

button_2.place(x=175.0, y=370.0, width=150.0, height=56.0)  # Posição centralizada

def on_enter(event):
    event.widget['bg'] = '#279645' 

def on_leave(event):
    event.widget['bg'] = '#32a852'

button_1.bind("<Enter>", on_enter)
button_1.bind("<Leave>", on_leave)
button_2.bind("<Enter>", on_enter)
button_2.bind("<Leave>", on_leave)

# Link para cadastro
# Função para sublinhar o texto quando o mouse passar por cima
def sublinhar(event):
    label_cadastro.config(font=("Roboto", 14, "underline"))  # Adiciona o sublinhado ao passar o mouse

# Função para remover o sublinhado quando o mouse sair
def remover_sublinhado(event):
    label_cadastro.config(font=("Roboto", 14))  # Restaura o estilo original

# Link para cadastro
label_cadastro = Label(window, text="Ainda não tenho uma conta", fg="#32a852", bg="#E6F4EA", font=("Roboto", 14), cursor="hand2")
label_cadastro.place(x=140.0, y=440.0)

# Bind dos eventos para sublinhar e remover o sublinhado
label_cadastro.bind("<Enter>", sublinhar)  # Ao passar o mouse
label_cadastro.bind("<Leave>", remover_sublinhado)  # Ao sair do mouse

# Ação do clique
label_cadastro.bind("<Button-1>", lambda e: abrir_tela_cadastro())

def carregar_imagem():
    try:
        # Carregar a imagem com PhotoImage
        imagem = PhotoImage(file="images/impressão.png")
        
        # Redimensionar a imagem
        imagem_redimensionada = imagem.subsample(4)  # Ajusta o fator de redimensionamento (aumente o número para diminuir mais)

        # Definir a imagem no label
        label_imagem.config(image=imagem_redimensionada)
        label_imagem.image = imagem_redimensionada  # Manter a referência para evitar coleta de lixo
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")


frame_nome_imagem = Frame(window, bg="#ffffff", width=220, height=40, bd=2, relief="solid")
frame_nome_imagem.place(x=140, y=313)  # Posicionando o frame abaixo do botão de "Selecionar"

# Label para exibir o nome da imagem selecionada dentro da caixinha
label_nome_imagem = Label(frame_nome_imagem, text="", bg="#ffffff", fg="#32a852", font=("Roboto", 14))
label_nome_imagem.place(x=10, y=5)  # Colocando o texto dentro da "caixinha"

# Configuração do label da imagem
label_imagem = Label(window, bg="#E6F4EA")
label_imagem.place(x=186, y=490)  # Posicionando a imagem abaixo do link

# Chamar a função para carregar e redimensionar a imagem
carregar_imagem()

window.resizable(False, False)
window.mainloop()
