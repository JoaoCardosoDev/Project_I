# Project I
============

### Objetivo
O objetivo deste projeto é criar uma aplicação web utilizando a framework Django, aplicação esta que permite o upload e download de ficheiros, criação de pastas e navegação entre elas, semelhante ao google drive.

### Organização do projeto
O projeto está organizado da seguinte maneira:

* `project_i/`: Pasta raiz do projeto, contendo os arquivos de configuração do Django, incluindo o arquivo `settings.py`.
* `EticDrive`: App que contem user based logic onde estão as funções que suportam o custom user criado.
* `filemanager`: App que contem toda a lógica de pastas e ficheiros e onde se encontra a grande parte do projeto.
* `filemanager/templates/`: Pasta que contém os templates HTML para a aplicação.
* `filemanager/static/`: Pasta que contém os arquivos estáticos, como CSS e JavaScript e imagens.


### Processo de Instalação


1. Clone o repositório do projeto: `git clone https://github.com/JoaoCardosoDev/Project_I.git`
2. Abra o terminal na pasta do projeto ou navegue até ela via (depende do contexto) `cd Project_I`.
3. Executar o comando `make up` para correr o projecto e instalar as dependencias.
4. Execute o comando `make superuser` caso seja a primeira utilização para criar uma conta admin.


### Comandos Makefile
* `make docker`: Corre o o docker.
* `make migration`: Cria as tabelas do banco de dados.
* `make superuser`: Cria um superuser para a aplicação.
* `make up`: Corre a aplicação.
* `make down`: Interrompe a aplicação.