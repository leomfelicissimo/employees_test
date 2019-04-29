# Leonardo's Django Coding Test #

## Getting Started ##

### Get the source code ###
```git clone https://github.com/leomfelicissimo/employees_test``` 

### Criar um usuário para o admin ###
docker exec -it empapp python manage.py createsuperuser --username admin

### Executar migrations ###
docker exec -it empapp python manage.py migrate

### Para rodar os testes ###
docker exec -it empapp python manage.py test
