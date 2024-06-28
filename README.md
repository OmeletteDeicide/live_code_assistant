# Code Assistant

## Description

Ce projet est une application web développée avec Django. Elle vise à aider le développement en Dart, Python ou Java

## Installation

Pour installer les dépendances de ce projet, veuillez exécuter la commande suivante :

```bash
pip install -r requirements.txt
```

ajouter un fichier .env ici : code_assistant\\.env
son contenu doit être : 
```
OPENAI_API_KEY='Votre clé API'
```

Changer settings.py :
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'votre_nom_de_db',
        'USER': 'votre_user_name',
        'PASSWORD': '_votre_user_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Utilisation

Après avoir installé les dépendances, vous pouvez lancer le serveur de développement en exécutant :

```bash
python manage.py runserver
```

Visitez http://127.0.0.1:8000/ dans votre navigateur pour voir l'application en action.