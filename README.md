# TP1
TP1 final clean code : API validation identifiant client 

# Déploiement
## 1. Environnement virtuel
### 1.1. Installation
Dans le répertoire local du projet précédemment téléchargé, créer à la racine un environnement virtuel python :
``` console
jo@LTPHP:/mnt/d/Workspace/Projets/TP1$ python3 -m venv 'nom_du_venv'
```
Documentation venv: https://docs.python.org/3/tutorial/venv.html
### 1.2. Sourcing
Une fois l'environnement virtuel installé, le sourcer avec la commande suivante sous linux:
``` console
jo@LTPHP:/mnt/d/Workspace/Projets/TP1$ source 'nom_du_venv'/bin/activate
```
ou sous Windows:
``` console
'nom_du_venv'/Script/activate.bat
```
### 3.3. Installation des dépendances
Une fois l'environnement virtuel démarré, installer les dépendances de l'API avec la commande suivante:
``` console
('nom_du_venv') jo@LTPHP:/mnt/d/Workspace/Projets/TP1$ pip install -r requirements.txt
```

## 2. Mise en service de l'API
Toujours à la racine du répertoire du projet, démarrer le serveur flask avec la commande suivante:
``` console
('nom_du_venv') jo@LTPHP:/mnt/d/Workspace/Projets/TP1$ python manage.py run
```
Le serveur flask démarre avec la trace suivante:
``` console
('nom_du_venv') jo@LTPHP:/mnt/d/Workspace/Projets/TP1$ python manage.py run
 * Serving Flask app "app.main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 470-652-628
```
## 3. Accéder à l'API
L'API peut être requêtée via curl sur la routes définies dans le TP (voir TP_F1.pdf et TP_F1 - Extension.pdf), ou bien via l'interface graphique de Swagger disponible sur
http://localhost:5000/

## 4. Éxecution des tests unitaires
Toujours à la racine du répertoire du projet, démarrer le serveur flask avec la commande suivante:
``` console
('nom_du_venv') jo@LTPHP:/mnt/d/Workspace/Projets/TP1$ python manage.py test
```
