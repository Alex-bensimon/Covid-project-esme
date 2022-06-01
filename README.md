# Covid-project-esme
Groupe : Baranzelli Lisa et Alcaraz Julien 

Introduction :

Projet réalisé dans le cadre de notre 4ème année en école d'ingénieur.

Ce projet permet de récupérer les données du covid depuis son existence selon les régions et les dates tout en mettant à jour quotidiennement les nouvelles données (cas hospitalisés, cas positifs, cas en réanimation..)

Comment fonctionne notre projet ?

Etape 1 : Récupérer toutes les données existantes 
- Pour ce faire vous aurez besoin de créer un compte GCP puis créer une base de données et une table dans BigQuery.
- Par la suite vous devez créer une clé credential que vous ajouterez dans votre dossier en local.
- Ajoutez de même projet_covid_full_data.py et executez le en specifiant le nom de votre clé ainsi que le nom de votre base de données et de votre table
- Exécutez le code 


Etape 2 : Récupérer les données de la veille
- Créez une Cloud function et mettez en code source celui contenu dans projet_covid_date_veille.py


Etape 3 : Exéctution du code quotidiennement 
- Allez dans Cloud scheduler et associer votre Cloud function a celui du scheduler (vous trouverez l'URL Cible dans Cloud function)
- Pensez à ajouter une fréquence d'éxécution (pour ce projet nous avons choisi de l'éxécuter tous les jours a 3h soit frequence : 0 3 * * *)


Etape 4 : La visualisation des données
- Le plus simple est de visualiser directement dans data studio ou vous pourrez créer un compte ou directement l'ouvrir depus BigQuery
- Faites des graphs, des camenberts ou affichez les cartes selon les régions et les dates


Remerciement à notre encadrant Alexandre Bensimon qui nous a accompagné et aidé lors de ce projet 
