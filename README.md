# TP1
TP1 final clean code : API validation identifiant client 

# Déploiement
## 1. Récupérer les sources en local avec un client git
``` git
git clone https://github.com/jduplaix/TP1.git
```


## 2. Environnement virtuel
### 2.1. Installation
Dans le répertoire local du projet précédemment téléchargé, créer à la racine un environnement virtuel python :
::: bash
python3 -m venv 'nom_du_venv'
:::
Documentation venv: https://docs.python.org/3/tutorial/venv.html
### 2.2. Sourcing
Une fois l'environnement virtuel installé, le sourcer avec la commande suivante sous linux:
``` bash
source 'nom_du_venv'/bin/activate
```
ou sous Windows:
``` powershell
'nom_du_venv'/Script/activate.bat
```
### 2.3. Installation des dépendances
Une fois l'environnement virtuel démarré, installer les dépendances de l'API avec la commande suivante:
``` bash
pip install -r requirements.txt
```

## 3. Mise en service de l'API
Toujours à la racine du répertoire du projet, démarrer le serveur flask avec la commande suivante:
``` bash
python manage.py run
```
Le serveur flask démarre avec la trace suivante:
``` bash
(venv) jo@LTPHP:/mnt/d/Workspace/Projets/TP1$ python manage.py run
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
## 4. Accéder à l'API
L'API peut être requêtée via curl sur la route 'localhost:5000/id/<ID à checker>', ou bienvia l'interface graphique de Swagger disponible sur
http://localhost:5000/

## 5. Éxecution des tests unitaires
Toujours à la racine du répertoire du projet, démarrer le serveur flask avec la commande suivante:
``` bash
python manage.py test
```
