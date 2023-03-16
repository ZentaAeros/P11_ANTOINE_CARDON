# Améliorez une application Web Python par des tests et du débogage
Bienvenue sur la plateforme numérique pour coordonner les compétitions de force réalisé par Güdlft

## Comment executer ce script sous Windows ?
* Veuillez créer un dossier à l'emplacement souhaité où sera placé le projet.
* Vous pouvez désormais clôner ce dépot dans le dossier fraîchement créé via `git clone https://github.com/ZentaAeros/P11_ANTOINE_CARDON.git`
* Vous pouvez à présent créer un environnement virtuel via : `python -m venv env`
* Activez l'environnement virtuel via `env/Scripts/activate`
* Installez les paquets nécessaire à l'éxecution du script à l'aide du fichier *requirements.txt* via `python -m pip install -r requirements.txt`
* Allez à la racine du projet via `cd P11_ANTOINE_CARDON`
* Executez cette commande `$env:FLASK_APP="server.py`
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
* Executez cette commande `export FLASK_APP=server.`
* Puis lancer le serveur via la commande `flask run`
* Utilisez votre navigateur internet favori et entrez cette URL : http://127.0.0.1:5000/
* ENJOY ! Vous êtes prêt à utiliser l'application !

## Lancer les tests unitaires / intégration
* Pour lancer les tests vous devez executer la commande `pytest`

* Exemple de rapport : 
> ========================================================================================================== test session starts ============================================================================================================
> platform win32 -- Python 3.10.10, pytest-7.2.2, pluggy-1.0.0
> rootdir: C:\Users\abcardon\Documents\openclassroom\projects\projet11\16032023\P11_ANTOINE_CARDON
> plugins: cov-4.0.0, flask-1.2.0
> collected 15 items
> 
> tests\integration_tests\test_deduct_points_clubs.py .                                                                                                                                                                                 [  6%]
> tests\units_tests\test_booking.py .......                                                                                                                                                                                             [ 53%]
> tests\units_tests\test_display_points_clubs.py .                                                                                                                                                                                      [ 60%] 
> tests\units_tests\test_login.py ....                                                                                                                                                                                                  [ 86%]
> tests\units_tests\test_logout.py .                                                                                                                                                                                                    [ 93%]
> tests\units_tests\test_remove_points_clubs.py .                                                                                                                                                                                       [100%] 
> 
> ============================================================================================================ 15 passed in 0.13s ============================================================================================================

## Lancer un test de couverture
Pour lancer un test de couverture veuillez executer cette commande : `pytest --cov=. --cov-report html`
Un nouveau dossier nommé "htmlcov" sera créé à la racine du projet, il suffira d'ouvrir le fichier "index.html" de ce dossier dans votre navigateur internet favori.
