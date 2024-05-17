# Pytonando
Projeto feito na semana Pythonando com Django
## Passo 1 
- Baixar as dependencias do projeto execute no terminal "pip install -r requirements.txt"
## Passo 2 
- Ative o ambiente virtual execute "venv\Scripts\Activate"
## Passo 3
- Caso for usar o banco de dados Sqlite3 va em na pasta Study_async em settings.py e descomente
 #'default': {
   #    'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': BASE_DIR / 'db.sqlite3',
   # }
}

E comente deixe como comentario essa parte
'default': dj_database_url.parse(
        'postgres://pytonando_user:CnPf9e72Oiyqv93nyqD4N85Jj9YJqCPS@dpg-cp2m4763e1ms73f1u87g-a.oregon-postgres.render.com/pytonando',
    )
## Passo 4
- Execute no terminal python manage.py runserver e va para o caminho indicado pelo comando



