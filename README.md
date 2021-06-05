# Instalação


## Download do projeto


```shell
git clone https://github.com/JacksonOsvaldo/birthday-navarra.git && cd birthday-navarra
```

## Instalação da Virtualenv

```shell
virtualenv -p python3.8 env && source env/bin/activate && pip install -U pip
```

## Instalação das dependências

```shell
pip install -r requirements.txt
```

## Executando as migrations


```shell
python manage.py makemigrations event
python manage.py migrate
```

## Caso queira, pode criar o super usuário

```shell
python manage.py createsuperuser
```

## Rodando o projeto
```shell
python manage.py runserver
```
