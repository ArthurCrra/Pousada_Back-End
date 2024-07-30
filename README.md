# 🏨 Projeto Quinta do Ypuá - API

Bem-vindo ao repositório do **Projeto Quinta do Ypuá**! Este projeto foi desenvolvido para solucionar problemas de administração de reservas e de finanças da pousada Quinta do Ypuá. O projeto foi realizado por um grupo de quatro alunos da faculdade utilizando a tecnologia **Flask** para o desenvolvimento do back-end.

## 🛠️ Instalação

Para rodar o projeto localmente, siga os passos abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/projeto-quinta-do-ypua-api.git
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    cd projeto-quinta-do-ypua-api
    python3 -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install flask psycopg2-binary
    ```

4. Inicie a aplicação:
    ```bash
    flask run
    ```

## 🎯 Objetivo

O objetivo principal deste projeto é melhorar a administração de reservas e a gestão financeira da pousada, proporcionando uma interface amigável e eficiente.

## 🚀 Tecnologias Utilizadas

- **Flask** - para a construção da API.
- **Python** - para a lógica de programação.
- **Psycopg2** - para a comunicação com o banco de dados PostgreSQL.
- **Marshmallow** - para serialização/deserialização de dados.

## 📄 Descrição do Projeto

A pousada Quinta do Ypuá estava enfrentando desafios significativos na administração de reservas e gestão financeira. Para resolver esses problemas, nosso grupo desenvolveu uma aplicação web com as seguintes funcionalidades:

- **Gerenciamento de Reservas**: Interface intuitiva para realizar e visualizar reservas.
- **Controle Financeiro**: Ferramentas para acompanhar receitas e despesas.
- **Criação e Remoção de Usuários**: Cadastro de novos usuários administradores do sistema para login individual.

