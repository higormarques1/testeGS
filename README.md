<h3>Desafio GS Ciência e Consumo</h3>
<h4><i>
Realizado o desenvolvimento de uma aplicação web utilizando Python + Django (templates), a aplicação
tem o intuito de realizar o cadastro, listagem, atualização e exclusão de produtos.
</i></h4>

<h3>Baixar o projeto:</h3>

1- git clone https://github.com/higormarques1/testeGS.git

<h3>Acesse a raiz do projeto e no terminal digite os seguintes comandos:</h3>

2- docker-compose run web python manage.py makemigrations

3- docker-compose run web python manage.py migrate

4- docker-compose run web python manage.py createsuperuser

5- docker-compose up -d

6- acesse do endereço 127.0.0.1:8000