# Como configurar PostgreSQL no Django
![Django](https://img.shields.io/badge/Django-v2.x-green.svg)

| Desenvolvimento:            | Professores:     | Disciplina:                    |
|-----------------------------|------------------|--------------------------------|
| Felipe Magalhães 14/0138374 | Edison Ishikawa  | Desenvolvimento de Aplicativos |
| Giovanni Guidini 16/0122660 | Marcio Victorino | CIC-122891                     |
| Vitor Dullens 16/0148260    |                  |                                |

## Instalações
1. Ativar seu virtualenv `source <name>/bin/activate`, como está nas [instruções](instructions.md);
2. [Baixar](https://www.postgresql.org/download/) e instalar o postgreSQL na sua maquina;
3. Agora instale psycopg2 - `pip install psycopg2` - para o django conseguir comunicar com o postgreSQL.

## Conexão

1. Abra uma nova aba no terminal e crie um DATABASE do postgreSQL:
```bash
$ sudo -i -u postgres
$ psql
$ create database <name>;
```
2. vá em [settings.py](/facapp/facapp/settings.py):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<name>',
        'USER': '<usr>',
        'PASSWORD': '<psw>',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
3. Faça as migrações conforme as intruções `python manage.py migrate`;
4. Para testar se deu certo, va no terminal do postgreSQL(1.)  e escreva `\dt`.
