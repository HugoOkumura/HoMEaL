# HoMEaL
Trabalho final da disciplina de Engenharia de Software da UTFPR.


## Instruções para a instalação do projeto

1. Clone o repositório:

    `git clone https://github.com/HugoOkumura/HoMEaL.git`


## 2. Para Contribuir no backend

2. 1. Acesse o diretório HoMEaL_backend/:

    `cd HoMEaL_backend/`

2. 2. Crie um ambiente virtual:

    `python3 -m venv .`

2. 3. Instale as dependências do backend:

    `pip3 install -r requirements.txt`

2. 4. Realize as alterações necessárias do banco:

    `python3 manage.py makemigrations`
    `python3 manage.py migrate`

## 3. Para Contribuir no frontend

3. 1. Acesse o diretório homeal_frontend:
    
    `cd homeal_frontend`

3. 2. Instale o pnpm:

    `npm install -g pnpm`

3. 3. Instale todas as dependências do frontend:

    `pnpm i`

3. 4. Crie um arquivo .env na raiz do frontend e digite o seguinte código:

    `NEXT_PUBLIC_API_URL=http://localhost:8000`


## 4. Para testar o projeto

4. 1. Instale o Docker Engine seguindo as instruções <a href="https://docs.docker.com/engine/install/">neste link</a>

4. 2. Na pasta raiz do projeto (HoMEaL/) suba o front e o back usando o comando:

    `sudo docker compose up` ou `sudo docker compose up -d` para a deixar em segundo plano

4. 3. Acesse os links no navegador para visualizar:
    
    `0.0.0.0:8000` para o backend
    `localhost:3000`para o frontend