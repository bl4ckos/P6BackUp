

# Mode d'emploi fichier Py

script de sauvegarde incrémentielle de donnée et restauration

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Script réalisé sur 2 serveurs Debian 9
Version Python 3

### Installing

Machine Wordpress :
installez le serveur LAMP
installez le serveur Wordpress

Les deux machines:

installez plugins SSH
#WARNING!#
Vous pouvez faire un échange de clé avec SSH pour une meilleur sécurité 
j'ai mi en place dans le fichier yaml une directive pour le mot de passe si besoin

## Pour une meilleur compréhension le backup script est commenté pour chaque ligne 

## Fichier YAML
Personnaliser les champs avec les **** ,
configuration save:

Adresse du serveur distant,
Nom d'utilisateur,

Indiquer un répértoire de backup,
Indiquer le répertoire de wordpress,

Configuration restore:
Adresse du serveur distant,
Nom d'utilisateur,
Mot de passe,
Indiquer le répertoire de wordpress,

## Deployment

- Veuillez mettre le fichier à la racine pour un test
- une fois mi en place utiliser crontab pour une sauvegarde journaliere 
en exemple : 0 0 * * * /home/***/fichier.py save backup.yaml

commande pour lancer une restore
./script.py restore backup.yaml

## Authors

* **Marvin Asselino** - *Initial work* - [bl4ckos](https://github.com/bl4ckos)
