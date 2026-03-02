# 🧠 Mentis - AI Interview Coach

O **Mentis** é um simulador de entrevistas de emprego técnico desenvolvido em Python, utilizando a tecnologia de IA generativa do **Google Gemini**. O objetivo é ajudar desenvolvedores a praticarem para entrevistas, recebendo perguntas dinâmicas baseadas na vaga e área de atuação desejada.

<p align="center">
  <img src="assets/banner-mentis.png" alt="Mentis Logo" width="100%">
</p>

---

## 🚀 Funcionalidades

- **Personalização:** Define o contexto da entrevista com base no nome da vaga e setor da empresa.
- **Interatividade:** Chat em tempo real com memória de contexto (o bot lembra o que você respondeu).
- **Segurança:** Filtros de segurança integrados para garantir um ambiente profissional.
- **Análise de currículo:** Carregue seu currículo para ser analisado e usado no seu treinamento para entrevistas

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)&nbsp;
![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)&nbsp;

---

## 📂 Estrutura do Projeto

```text
Mentis/
├── src/
│   ├── functions       
│   ├── ├── read_pdf.py # Leitura de currículo para análise
│   ├── config.py       # Configurações de IA e validação
│   ├── interview.py    # Lógica do motor de entrevista
├── .env                # Variáveis sensíveis (não versionado)
├── .gitignore          # Arquivos ignorados pelo Git
├── main.py             # Ponto de entrada da aplicação
└── requirements.txt    # Dependências do projeto
```

## ⚙️ Como Instalar e Rodar

Siga os passos abaixo para configurar o ambiente do **Mentis** em sua máquina local.

### 1. Clonar o Repositório

```bash
git clone https://github.com/HermandoThiago/simulador-entrevista-ia.git
cd mentis-ai-interviewer
```

### 2. Configurar o Ambiente Virtual (venv)

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar no Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# Ativar no Linux ou macOS:
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente

O Mentis precisa da sua chave de API para funcionar.
- Crie um arquivo chamado .env na raiz do projeto.
- Adicione a seguinte linha no arquivo:

```dotenv
GEMINI_AI_KEY=SUA_CHAVE_AQUI
```

### 5. Executar o Projeto

```python
python main.py
```
