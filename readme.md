# ApyTwitter

# Présentation
ApyTwitter est une application collectant les tweets les plus récents en fonction de mots-clés renseignés par l'utilisateur.
Ces mots-clés sont stockés dans une liste de "Filtres" persistants à chaque redémarrage.
Les tweets pourront également être précédés de "Flags" en fonction des mots présents dans le tweet pour permettre un tri plus aisé.

# Installation
## Python
La version de Python utilisée pour le développement de cette application est la 3.5 que l'on peut télécharger ici :

https://www.python.org/downloads/

## Django
Django peut être facilement installer à l'aide de l'installateur de packet de python : pip
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
Il existe deux modes de recherche:

-> La barre de recherche rapide, permettant d'afficher directement les tweets les plus récents contenant les mots-clés renseignés. Les mots-clés devront être séparés par un espace.

-> Les filtres: chaque filtre est lié à une liste de mots-clés renseignée à la création du filtre. Le bouton reload permettant de relancer la recherche de tweets associée à ces mots clés. 

## Création d'un nouveau filtre
Pour créer un nouveau filtre, il faut appuyer sur le bouton "Nouveau Filtre" et renseigner les champs "Nom du filtre" et "Mots-clés". Les mots-clés successifs devront être séparés par un espace.

## Création d'un nouveau flag
Pour créer un nouveau flag, il faut appuyer sur le bouton "Nouveau Flag" et renseigner les champs "Nom du flag" et "Mots-clés". Les mots-clés successifs devront être séparés par un espace.


# Précisions techniques
## Limites inhérentes à l'API Twitter
-> Suite à une mise à jour récente, le texte des tweets trop long ne s'affiche pas en entier.

-> Lors d'une recherche, certains tweets ne semblent pas contenir les mots-clés du filtre. Cela concerne les tweets contenant un lien. 
En effet, l'API Twitter recherche les mots-clés dans le texte du tweet mais également dans l'aperçu de cet éventuel lien.

-> Un filtre ne peut pas contenir plus de 500 mots-clés différents.

## Choix de Django et de Bootstrap
Pour développer nos compétences, nous avons décidé de travailler sur ces deux frameworks de développement web très utilisés.

-> Django: Le plus gros framework de développement web en Python.

-> Bootstrap: Rapide à prendre en main, facile d'utilisation et proposant de beaux designs. 

## Choix modèles/classes
Dans ce projet, il y a redondance entre les classes python et les modèles Django. Cela vient du fait que nous avons commencé ce projet en ligne de commande en utilisant des classes avant de passer sous Django.

## Nombre de tweets affichés
Nous avons pensé rajouter la fonction de nombre de tweets affichés sur la page (la notion de count est d'ailleurs présent à plusieurs endroits du code). 
Mais finalement, cela ne nous a pas semblé pertinent d'un point de vue UX due aux limitiations de l'API (100 tweets max affichés par requête).

## Persistence des données
La présence d'une BDD interfacée avec Django permet la persistence des différents filtres et flags.
Cependant, nous avons laissé la possibilité de faire une recherche sans sauvegarde de filtre grâce à la barre de recherche rapide. 

## Warning: Utilisation de la BDD
Si une erreur passe dans la BDD, cela peut empêcher le programme de démarrer (conflits d'urls). Dans ce cas, il faut re-télécharger une version antérieure et fonctionnelle de la BDD.

## Modification de filtre/flag
L'ajout de la fonction modification d'un filtre ou d'un flag ne nous semblait pas nécessaire. Pour faire une modification, il suffit de supprimer l'élement et d'en recréer un nouveau.

## Multithreading
Nous n'avons pas vu la pertinence du multithreading dans ce projet. Le point limitant aurait été la collecte des tweets, partie très bien gérée par l'API Twitter.

## Factory Pattern

