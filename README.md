# AppSecurity

Aplicação FastAPI que disponibiliza uma tela web para cadastro de usuários do aplicativo móvel.

## Pré-requisitos

- Python 3.11+
- `pip` para instalar dependências

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows use `.venv\\Scripts\\activate`
pip install -r requirements.txt
```

## Executando o servidor

```bash
uvicorn app.main:app --reload
```

Acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) para visualizar a tela de cadastro.

## Estrutura do projeto

```
app/
├── __init__.py
├── main.py          # Aplicação FastAPI e validação dos dados do formulário
├── static/
│   └── css/
│       └── styles.css
└── templates/
    └── register.html
```
