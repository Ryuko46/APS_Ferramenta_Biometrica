# 🔐 Ferramenta Biométrica com Impressão Digital

Sistema de autenticação biométrica utilizando **impressões digitais**, desenvolvido com Python, OpenCV e MySQL. A aplicação permite **cadastrar e autenticar usuários** por meio da extração e comparação de características únicas (minúcias) de impressões digitais.

---

## 📌 Descrição Geral

O objetivo do sistema é **verificar se duas impressões digitais pertencem à mesma pessoa**, utilizando técnicas de **visão computacional**, **extração de características**, **normalização de dados** e **comparação por similaridade vetorial**. O sistema é construído com uma arquitetura monolítica simples e clara, integrando front-end (GUI) com back-end em Python.

---

## 🚀 Funcionalidades

- 📸 **Leitura e pré-processamento de imagem** (escala de cinza com OpenCV)
- 🔍 **Extração de minúcias** (terminações e bifurcações) com Fingerprint Feature Extractor
- ♻️ **Limpeza e transformação de dados** de hexadecimal para inteiro (usando regex)
- 🧠 **Comparação vetorial de similaridade** com *cosine similarity* via `sklearn`
- 🗄️ **Armazenamento de usuários e características** em banco MySQL
- 🧑‍💼 **Interface gráfica com Tkinter** para cadastro e login biométrico
- ✅ **Validação de autenticação** com base em similaridade mínima

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- [OpenCV](https://opencv.org/) – Processamento de imagem
- [Fingerprint Feature Extractor](https://github.com/Utkarsh-Deshmukh/Fingerprint-Feature-Extraction) – Extração de minúcias
- **MySQL** – Banco de dados relacional
- **NumPy** – Normalização e manipulação de arrays
- **Regex (re)** – Limpeza de strings hexadecimal
- **Tkinter** – Interface gráfica (front-end)
- **Sklearn (cosine similarity)** – Comparação vetorial

---

## 🖼️ Estrutura de Telas e Arquivos

O sistema é dividido em arquivos principais, cada um responsável por uma parte do fluxo:

```
📁 FerramentaBiometrica/
├── main.py              # Tela principal / Navegação
├── cadastro.py          # Tela de cadastro biométrico
├── login.py             # Tela de login/autenticação
├── telasucesso.py       # Tela exibida após login bem-sucedido
├── banco.py             # Conexão e manipulação de dados no MySQL
├── comparador.py        # Função que compara as características
└── requirements.txt     # Lista de dependências
```

---

## ⚙️ Como Executar o Projeto
1. Clone o repositório:

```
git clone https://github.com/Ryuko46/FerramentaBiometrica.git
cd FerramentaBiometrica
Crie um ambiente virtual (opcional, mas recomendado):
```

2. Crie um ambiente virtual (opcional):

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Instale as dependências:
```

3. Instale as dependências:

```
pip install -r requirements.txt
Configure o banco MySQL:
```

4. Configure o banco MySQL:

-Crie o banco de dados e tabelas conforme estrutura usada no banco.py

-Altere as credenciais de conexão no código, se necessário

5. Execute a aplicação:

```
python main.py
```

---

## 📌 Observações:

-O sistema foi feito com fins educacionais e pode ser expandido para uso real com ajustes em segurança e escalabilidade.

-A comparação biométrica é feita com base na similaridade de cosseno entre vetores de minúcias extraídas de imagens.

-Imagens de baixa qualidade, sujeira ou ruído podem comprometer a precisão do reconhecimento.

---

## 👨‍💻 Autores

João Victor Crisci [(Ryuko46)](https://github.com/Ryuko46) 

Guilherme Vieira [(guilhermeAbbenante)](https://github.com/guilhermeAbbenante) 

Bruno da Silva [(E3ND)](https://github.com/E3ND) 

Hitalo Chaves [(Hitalo-27)](https://github.com/Hitalo-27) 
