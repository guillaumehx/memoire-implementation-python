
# Implémentation Python

Le programme Python s'exécute facilement en ligne de commande.

La première étape consiste à télécharger ou cloner le dépôt. Deux options sont possibles :
- Cliquer sur le bouton vert en haut à droite ```<> Code``` puis ```Download ZIP```.
- Ou utiliser git : ``` git clone https://github.com/guillaumehx/memoire-implementation-python.git ```

Une fois le repository sur votre machine, rendez-vous à la racine et suivez les étapes selon votre système.

Pour Python, il est nécéssaire d'avoir Python 3.

## Windows
### 1. Setup
Ouvrez un ``cmd`` à la racine et vérifiez que Python 3 n'est pas déjà installé en lançant la commande : ```python3 --version```
- Si rien ne s'affiche ou que la version n'est pas la bonne, rendez-vous sur le site https://www.python.org/downloads/ et téléchargez une version supérieur à 3.9 (peu importe)

Lors de l'installation, assurez-vous de de cocher la case **Add Python to PATH**

### 2. Exécution

Pour exécuter le programme, lancez ```python3 main.py "<ARGUMENT>"``` en remplacent ```<ARGUMENT>``` par une expression arithmétique, par exemple ```6+2*(10/5)``` et l'output sera ```10```.
Vous pouvez chaîner les arguments par un espace : ```python3 main.py "6+2*(10/5)" "2+2" "8-5^2"``` L'output sera alors
~~~~
10
4
-17
~~~~

## Linux
### 1. Setup
Ouvrez un terminal à la racine et vérifiez que Python 3 n'est pas déjà installé en lançant la commande : ```python3 --version```
- Si rien ne s'affiche ou que la version n'est pas la bonne : ```sudo apt install python3 python3-pip```

### 2. Exécution

Pour exécuter le programme, lancez ```python3 main.py "<ARGUMENT>"``` en remplacent ```<ARGUMENT>``` par une expression arithmétique, par exemple ```6+2*(10/5)``` et l'output sera ```10```.
Vous pouvez chaîner les arguments par un espace : ```python3 main.py "6+2*(10/5)" "2+2" "8-5^2"``` L'output sera alors
~~~~
10
4
-17
~~~~


## macOS
### 1. Setup
Ouvrez un terminal à la racine et vérifiez que Python 3 n'est pas déjà installé en lançant la commande : ```python3 --version```
- Si rien ne s'affiche ou que la version n'est pas la bonne, rendez-vous sur le site https://www.python.org/downloads/macos/ et téléchargez une version supérieur à 3.9 (peu importe)

### 2. Exécution

Pour exécuter le programme, lancez ```python3 main.py "<ARGUMENT>"``` en remplacent ```<ARGUMENT>``` par une expression arithmétique, par exemple ```6+2*(10/5)``` et l'output sera ```10```.
Vous pouvez chainer les arguments par un espace : ```python3 main.py "6+2*(10/5)" "2+2" "8-5^2"``` L'output sera alors
~~~~
10
4
-17
~~~~