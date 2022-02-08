# Mutation Analyzer

<!-- Adicionar descrição do projeto -->

## Estrutura do Projeto

```bash
.
├── Dockerfile
├── README.md
├── docker-compose.yml
├── entrypoint.sh
├── infra
│   ├── nginx
│   │   └── default.conf.template
│   └── uwsgi
│       └── mutation-analyzer-uwsgi.ini
├── manage.py
├── mutation_analyzer
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── helpers.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_create_superuser.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── tree

6 directories, 26 files
```

## Tecnologias utilizadas

- Python 3.8
- Django 4.0.2
- PostgreSQL (_Latest_)
- Nginx (_Latest_)
- uWSGI
- Docker 20.10.12
- Docker Compose 1.29.2

## Ferramentas utilizadas

- _Windows 10_
- _Ubuntu 20.04 LTS (WSL2)_
- _Visual Studio Code_

## Execução do projeto (_Docker Compose_)

Gerar o _build_ do projeto a partir do arquivo _docker-compose.yml_:

```sh
    docker-compose build
```

Iniciar os containers do _NGINX_, _PostgreSQL_ e _Aplicação_:

```sh
    docker-compose up -d
```

O serviço estará disponível em [http://localhost/](http://localhost/).