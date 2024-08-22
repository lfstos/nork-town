# Car App

Este é um aplicativo da web baseado em Django que permite aos usuários gerenciar uma lista de proprietários de automóveis e seus carros.

## Funcionalidades

- Listar todos os carros cadastrados
- Criar um novo carro e um novo proprietário
- Visualizar, atualizar e excluir um carro específico e um proprietário

## Pré-requisitos
- Docker e Docker Compose instalados no seu computador

## Começando
    1. git clone git@github.com:lfstos/nork-town.git
    2. cd nork-town
    3. python -m venv .venv
    4. source .venv/bin/activate
    5. pip install -r requirements.txt

# Construa e inicie os contêineres Docker:
docker-compose up -d

# Aplique as migrações do banco de dados:
docker-compose run web python manage.py migrate
Isso irá criar e iniciar os contêineres necessários para o aplicativo, incluindo o banco de dados PostgreSQL, e criar as tabelas necessárias no banco de dados.

## Uso:
Acesse http://localhost:8000

## Exemplos:
http://localhost:8000/api/cars/
Você verá a lista de carros cadastrados.
Para criar um novo carro, envie uma requisição POST para o endpoint /api/cars/ com os seguintes dados:
json

## Copiar código
```
{
  "color": "yellow",
  "model": "hatch",
  "owner": 1
}
```
Para visualizar, atualizar ou excluir um carro específico, use os seguintes endpoints:
- Visualizar: GET /api/cars/<id>/
- Atualizar: PUT /api/cars/<id>/
- Excluir: DELETE /api/cars/<id>/
- Substitua <id> pelo ID do carro que você deseja manipular.

## Testes

Para executar os testes unitários, use o seguinte comando:


## Tecnologias Utilizadas
- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Docker Compose
- Estrutura do Projeto

```
car-app/
├── car_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── Dockerfile
├── docker-compose.yml
├── manage.py
└── README.md
```
## Contribuição

Sinta-se à vontade para contribuir com o projeto, reportar problemas ou sugerir melhorias. Basta abrir uma nova issue ou enviar um pull request.