# Covid-project-esme
Groupe : Baranzelli Lisa et Alcaraz Julien 

Introduction :

Projet réalisé dans le cadre de notre 4ème anée en école d'ingénieur.

Ce projet permet de recuperer les données du covid depuis son existence selon les regions et les dates tout en mettant a jour quotidiennement les nouvelles données (cas hospitalisé, cas positif, cas en réanimation..)

Comment fonctionne notre projet ?

Etape 1 : Récupérer toutes les données existantes 
- Pour se faire vous aurez besoin de creer un compte GCP puis creer une base de données et une table dans BigQuery.
- Par la suite vous devez creer une clé credential que vous ajouterez dans votre dossier en local.
- Ajoutez de meme projet_covid_full_data.py et executez le en specifiant le nom de votre clé ainsi que le nom de votre base de données et de votre table
- Executez le code 

Etape 2 : Récupérez les données de la veille
- Creez une Cloud function et mettez en code source celui contenu dans projet_covid_date_veille.py

Etape 3 : Exectution du code quotidiennement 
- Allez dans Cloud scheduler et associé votre Cloud function a celui du scheduler (vous trouverez l'URL Cible dans Cloud function)
- pensez a ajoutez une frequence d'execution (pour ce projet nous avons choisi de l'executer tous les jours a 3h soit frequence : 0 3 * * *)

Etape 4 : La visualisation des données
- Le plus simple est de visualiser directement dans data studio ou vous pourrez creer un compte ou directement l'ouvrir depus BigQuery
- faites des graphs, des camenbert ou affichez les cartes selon les regions et les dates


Remerciement a notre encadrant Alexandre Bensimon qui nous a accompagné et aidé lors de ce projet 