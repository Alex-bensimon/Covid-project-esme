# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:32:54 2022

@author: alcje
"""

from google.cloud import bigquery
import datetime
import json
import os 
import requests

date = datetime.date.today()  # date du jour
date_veille = date + datetime.timedelta(-1)  # date de la veille
format_date_veille_url = date_veille.strftime("%d-%m-%Y") 
format_date_veille_titre = date_veille.strftime("%d_%m_%Y")

with open(f"data_veille_{format_date_veille_titre}.json", "w") as mon_fichier:
    url = (
           f"https://coronavirusapifr.herokuapp.com/data/departements-by-date/{format_date_veille_url}"
           )
    reponse = requests.get(url)
    reponse_content = reponse.json()
    for content in reponse_content:
        mon_fichier.write(json.dumps(content) + "\n")


#ON SE CONNECTE A GCP
credentials_path = 'C:/Users/alcje\Desktop/2D/Covid_project_esme/gcp_credentials.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=credentials_path

client = bigquery.Client()  # creation d'un nouveau client qui utilise GCP
dataset_id = "covid_data_esme" 
table_id = "all_data_esme"
dataset_ref = client.dataset(dataset_id) #on se connect a la data set puis a la table 
table_ref = dataset_ref.table(table_id)

# configuration
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON#on le prend ligne par ligne 
job_config.autodetect = True #il detecte automatiquement les clés de la table 
job_config.write_disposition = "WRITE_APPEND" #ECRIT EN AJOUTANT 

with open(f"data_veille_{format_date_veille_titre}.json", "rb") as mon_fichier :
    job = client.load_table_from_file (
        mon_fichier,
        table_ref,
        location="europe-west1",
        job_config = job_config
        )
    
print("Les données ajoutées a la table {}".format(table_ref))



