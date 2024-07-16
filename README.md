# 🍽️ Aplicativo de Restaurante em Python com POO e FastAPI

## ✉️ Sobre

Este projeto é uma aplicação que simula o gerenciamento de um restaurante, permitindo aos usuários registrar novos restaurantes, listar os existentes, alternar seu estado (ativo/desativado), registrar avaliações e acessar cardápios por meio de uma API desenvolvida com FastAPI.

## 🚀 Tecnologias

<div>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/Requests-0074D9?style=for-the-badge&logo=requests&logoColor=white">
</div>


## 📸 Imagem do projeto

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/986b376d-065c-45e6-aca4-17c6d583066a" alt="imagem do projeto" width="500"></td>
    <td><img src="https://github.com/user-attachments/assets/8f45c7ac-62d5-4031-ae78-3d2250709e83" alt="imagem do projeto" width="500"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/752a6695-dbde-4932-b665-0c25ca8f4da5" alt="imagem do projeto" width="500"></td>
    <td><img src="https://github.com/user-attachments/assets/55080e7a-1d82-411f-bc2b-5fb33eb48d2d" alt="imagem do projeto" width="500"></td>
  </tr>
</table>

## 🔨 Funcionalidades do projeto

- **Cadastro de Restaurantes**: Permite ao usuário adicionar novos restaurantes à lista.
- **Listagem de Restaurantes**: Exibe todos os restaurantes cadastrados com suas respectivas categorias, avaliações e estado (ativo/desativado).
- **Alteração de Estado**: Permite ao usuário alterar o estado de um restaurante (ativo/desativado).
- **Registro de Avaliações**: Permite ao usuário registrar avaliações para os restaurantes.
- **Cálculo da Média de Avaliações**: Calcula e exibe a média das avaliações para cada restaurante.
- **API para Cardápios**: Permite acessar cardápios dos restaurantes via endpoints da API FastAPI.

## ✔️ Técnicas e tecnologias utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver a lógica do aplicativo.
- **FastAPI**: Framework web utilizado para criar a API REST.
- **Requests**: Biblioteca utilizada para realizar requisições HTTP.
- **JSON**: Utilizado para salvar e manipular os dados dos cardápios.

## ⚙️ Como Funciona

1. **Criação de Restaurantes**: Permite ao usuário criar novos restaurantes com nome e categoria.
2. **Listagem de Restaurantes**: Exibe todos os restaurantes cadastrados, suas categorias, estado e média de avaliações.
3. **Alteração de Estado**: Permite ao usuário alternar o estado de um restaurante entre ativo e desativado.
4. **Registro de Avaliações**: Permite ao usuário registrar avaliações para os restaurantes, garantindo que a nota esteja no intervalo de 1 a 10.
5. **Cálculo da Média de Avaliações**: Calcula a média das notas de avaliações de cada restaurante.
6. **API para Cardápios**: Disponibiliza endpoints para exibir mensagens e cardápios dos restaurantes.

## 🛠️ Como Usar

1. Clone o repositório para sua máquina local.
   ```
   git clone https://github.com/SeuUsuario/Aplicativo-Restaurante-POO.git
2. Navegue até o diretório do projeto.
   ```
   cd Aplicativo-Restaurante-POO
3. Crie um ambiente virtual e ative-o.
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
4. Instale as dependências listadas em requirements.txt.
   ```
   pip install -r requirements.txt
5. Execute o script app.py para inicializar a aplicação de terminal.
    ```
    python app.py
6. Execute o script main.py para inicializar a API FastAPI
   ```
   uvicorn main:app --reload
7. Acesse os endpoints da API
   ```
   GET /api/hello - Exibe uma mensagem simples.
   GET /api/restaurantes/ - Exibe os cardápios dos restaurantes. Use o parâmetro restaurtante para filtrar por restaurante.

## Time
<img loading="lazy" src="https://avatars.githubusercontent.com/u/34192862?s=400&u=e8511485b428717385e3ae9483ade57359be8779&v=4" width=115><br><sub>Arruda Júnior</sub>
