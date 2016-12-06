# ApyTwitter

# Présentation

# Installation
## Python
La version de Python utilisée pour le développement de cette application est la 3.5 que l'on peut télécharger ici :

## Django
Django peut être facilement installer à l'aide dl'intallateur de packet de pyhton : pip
```bash
pip install django
```
Attention, il est nécessaire d'éxécuter cette commande en tant qu'administrateur
## Base de données

# Configuration
## API Twitter
Pour pouvoir communiquer avec l'API Twitter, il est nécessaire d'obtenir les clés de connexion auprès de Twitter.
Ces clés, une fois obtenue doivent être placées dans un fichier config.py située dans le repertoire
```bash
./apyTwitter/tweetsChecker/controllers
```
Le fichier config.py doit être de la forme :
```python
userKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
secretKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

# Utilisation
## Lancer l'application
Pour lancer l'application, il faut executer le fichier manage.py localisé dans le dossier apyTwitter, de la façon suivante :
```bash
python manage.py runserver
```
Il est ensuite possible d'accéder à l'application depuis un navigateur en allant à l'adresse:
http://localhost:8000/tweetsChecker
## Recherche
## Création d'un nouveau filtre
## Création d'un nouveau flag
