# Améliorez une application Web Python par des tests et du débogage
Bienvenue sur la plateforme numérique pour coordonner les compétitions de force réalisé par Güdlft

## Comment executer ce script sous Windows ?
* Veuillez créer un dossier à l'emplacement souhaité où sera placé le projet.
* Vous pouvez désormais clôner ce dépot dans le dossier fraîchement créé via `git clone https://github.com/ZentaAeros/P11_ANTOINE_CARDON.git`
* Vous pouvez à présent créer un environnement virtuel via : `python -m venv env`
* Activez l'environnement virtuel via `env/Scripts/activate`
* Installez les paquets nécessaire à l'éxecution du script à l'aide du fichier *requirements.txt* via `python -m pip install -r requirements.txt`
* Allez à la racine du projet via `cd P11_ANTOINE_CARDON`
* Executez cette commande `$env:FLASK_APP="server.py"`
* Puis lancer le serveur via la commande `flask run`
* Utilisez votre navigateur internet favori et entrez cette URL : http://127.0.0.1:5000/
* ENJOY ! Vous êtes prêt à utiliser l'application !

## Comment executer ce script sous MacOS ?
* Veuillez créer un dossier à l'emplacement souhaité où sera placé le projet.
* Vous pouvez désormais clôner ce dépot dans le dossier fraîchement créé via `git clone https://github.com/ZentaAeros/P11_ANTOINE_CARDON.git`
* Vous pouvez à présent créer un environnement virtuel via : `python -m venv env`
* Activez l'environnement virtuel via `source env/bin/activate`
* Installez les paquets nécessaire à l'éxecution du script à l'aide du fichier *requirements.txt* via `python -m pip install -r requirements.txt`
* Allez à la racine du projet via `cd P11_ANTOINE_CARDON`
* Executez cette commande `export FLASK_APP=server`
* Puis lancer le serveur via la commande `flask run`
* Utilisez votre navigateur internet favori et entrez cette URL : http://127.0.0.1:5000/
* ENJOY ! Vous êtes prêt à utiliser l'application !

## Lancer les tests unitaires / intégration
* Pour lancer les tests vous devez executer la commande `pytest`

## Lancer un test de couverture
* Veuillez executer cette commande : `pytest --cov=. --cov-report html`

Un nouveau dossier nommé "htmlcov" sera créé à la racine du projet, il suffira d'ouvrir le fichier "index.html" de ce dossier dans votre navigateur internet favori.

## Lancer un test de performance
*Il faut au préalable lancer le serveur flask, pour cela veuillez suivre les instructions ci-dessus selon votre OS*
* Executer cette commande : `locust -f tests/performance_tests`
* Se rendre sur son navigateur internet favori et entrer l'URL suivante : http://0.0.0.0:8089/ 
* Dans le champs *Number of users* veuillez saisir : 6
* Dans le champs *Host* veuillez saisir : http://127.0.0.1:5000
* Cliquez sur *Start swarming* et vous verrez ainsi le résultat
