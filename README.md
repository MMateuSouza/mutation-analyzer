# Mutation Analyzer

Projeto que detecta se uma sequência de DNA pertence a um humano ou a um mutante.

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

## Utilização da API

A API possui dois *endpoints*, um para análise de DNA e outro de análise estatísticas (Quantidade de DNAs mutantes e humanos, além da relação de DNAs mutantes entre os humanos).

### Análise de DNA mutante

#### Request

`POST /mutants/`

```json
{
  "dna": ["CTGGAA", "CTGCTC", "TGCTGT", "AGAGGG", "TCCCTA", "TCACTG"]
}
```

> A chave `dna` é **obrigatória**.

#### Response

```json
{"success": false, "is_valid": true, "message": "O DNA informado é válido."}
```

> `success`: Especifica se a análise foi um DNA mutante ou humano. (`false` é humano, `true` é mutante).

> `is_valid`: Especifica se o DNA enviado é uma cadeira válida.

> `message`: Um *feedback* verboso.

### Estatísticas

#### Request

`GET /stats/`
#### Response

```json
{"count_mutants_dna": 0, "count_human_dna": 0, "ratio": 0}
```
> `count_mutants_dna`: Quantidade de DNAs mutantes analisados.

> `count_human_dna`: Quantidade de DNAs humanos analisados.

> `ratio`: Relação entre DNAs mutantes e humanos.
