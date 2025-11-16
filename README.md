# Classificador de E-mails

Aplicação web para classificação de e-mails usando inteligência artificial (OpenAI).

## Ideia inicial

[!Imagem da ideia](./public/excalidraw1.png)

## Wireframe

### Tela inicial

[!Tela 1](./public/excalidraw3.png)

### Tela de loading

[!Tela 2](./public/excalidraw2.png)

### Tela do resultado

[!Tela 3](./public/excalidraw4.png)

## Protótipo do Figma

### Tela inicial

[!Tela 1](./public/figma1.png)

### Tela de loading

[!Tela 2](./public/figma2.png)

### Tela do resultado

[!Tela 3](./public/figma3.png)


## Links

- [Protótipo no Figma](https://www.figma.com/design/z0hEG5cva8iCiQvGIOutFe/Classificador-de-E-mails?node-id=0-1&t=FiYDBOKomLMlqtTo-1)
- [Diagrama no Excalidraw](https://excalidraw.com/#json=WJPsAlDx6BCBCRBFRd-MY,It6vF9kdJzcV2bmsAathtQ)

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Uma chave de API da OpenAI

## 🚀 Como Rodar o Projeto

### 1. Clonar o Repositório

```bash
git clone <url-do-repositorio>
cd classificador
```

### 2. Criar um Ambiente Virtual (Recomendado)

**No Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**No macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
OPENAI_API_KEY=sua_chave_de_api_aqui
HOST=127.0.0.1
PORT=5000
DEBUG=False
```

**Importante:** Para obter sua chave de API da OpenAI, visite [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### 5. Executar a Aplicação

```bash
python run.py
```

A aplicação estará disponível em: **http://127.0.0.1:5000**

## 📁 Estrutura do Projeto

```
classificador/
├── app/
│   ├── __init__.py           # Inicialização da aplicação Flask
│   ├── email_classifier.py   # Lógica de classificação
│   ├── routes.py             # Rotas da API
│   ├── static/
│   │   └── style.css         # Estilos da interface
│   └── templates/
│       └── index.html        # Interface web
├── config.py                 # Configurações da aplicação
├── run.py                    # Ponto de entrada
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo
```