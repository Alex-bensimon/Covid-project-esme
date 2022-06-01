import json
import pandas as pd
import requests
from google.cloud import bigquery
import os

data = pd.read_csv("departements-france.csv")
# print(data['nom_departement'])

with open("data_full.json", "w") as mon_fichier:
    # num_dep = int(input("choisir un numero de departement"))
    region = data["nom_departement"].tolist()
    dep_a_eviter = ["Corse-du-Sud", "Haute-Corse"]
    for r in region:
        if r not in dep_a_eviter:
            try:
                reponse = requests.get(
                    "https://coronavirusapifr.herokuapp.com/data/departement/" 
                    + r.lower()
                ) 
                reponse_content = reponse.json()  # mettre en dictionnaire
                for content in reponse_content:
                    mon_fichier.write(json.dumps(content) + "\n")
            except ValueError as e:  # pas coonu -> ressort dep inconnu
                print(e)

#ON SE CONNECTE A GCP
credentials_path = 'C:/Users/julma/Desktop/Covid_project_esme/gcp_credentials.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=credentials_path

client = bigquery.Client()  # creation d'un nouveau client qui utilise GCP
dataset_id = "covid_data_esme" 
table_id = "all_data_covid"
dataset_ref = client.dataset(dataset_id) #on se connect a la data set puis a la table 
table_ref = dataset_ref.table(table_id)

# configuration
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON#on le prend ligne par ligne 
job_config.autodetect = True #il detecte automatiquement les clés de la table 
job_config.write_disposition = "WRITE_TRUNCATE" #ECRIT EN ECRASANT 

with open("data_full.json", "rb") as mon_fichier :
    job = client.load_table_from_file (
        mon_fichier,
        table_ref,
        location="europe-west1",
        job_config = job_config
        )
    
print("Les données ajoutées a la table {}".format(table_ref))
