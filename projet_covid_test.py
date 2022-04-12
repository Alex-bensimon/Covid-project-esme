# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:32:54 2022

@author: alcje
"""

import json
import datetime


date = datetime.date.today()#date du jour
date_veille=date + datetime.timedelta(-1)#date de la veille 

with open('data_full.json','r') as sample:#j'ouvre le json avec toutes les données
    for line in sample: #on load chaques lignes
        line = json.loads(line.strip())
        if str(line['date'])==str(date_veille): #si une date du fichier json correspond a la date d'hier, on retourne toute la ligne
            print(line)



#test envoyer sur big query(pas finalisé)
'''
from google.cloud import bigquery
client = bigquery.Client()#creation d'un nouveau client qui utilise GCP
dataset_id = "data"#on prepare une ref a un dataset pour stocker les requetes 
data_projet = "covid-projet-esme"
dataset_id_full = f"{client.data_projet}.{dataset_id}"#f"{client.project}.{dataset_id}"
dataset = bigquery.Dataset(dataset_id_full)

dataset = client.create_dataset(dataset)#creation d'une data set sur bigquery 

#configuration 
job_config = bigquery.QueryJobConfig()
job_config.destination = f"{dataset_id_full}.regression_input"

sql = """
    SELECT corpus
    FROM `bigquery-public-data.samples.shakespeare`
    GROUP BY corpus;
"""

query_job = client.query(sql, job_config=job_config)
query_job.result()

print("Query results loaded to the table {}".format(dataset_id_full))
'''