from google.cloud import bigquery
import datetime
import json
import os 
import requests
from os import path

def ingestion(request):
    date = datetime.date.today()  # date du jour
    date_veille = date + datetime.timedelta(-1)  # date de la veille
    format_date_veille_url = date_veille.strftime("%d-%m-%Y") 
    format_date_veille_titre = date_veille.strftime("%d_%m_%Y")

    root = path.dirname(path.abspath(__file__))
    file_path = f"/tmp/data_veille_{format_date_veille_titre}.json"

    with open(path.join(root, file_path), "w") as mon_fichier:
        url = (
           f"https://coronavirusapifr.herokuapp.com/data/departements-by-date/{format_date_veille_url}"
           )
        reponse = requests.get(url)
        reponse_content = reponse.json()
        for content in reponse_content:
            if content == reponse_content[28] or content == reponse_content[29]: 
                print("error")
            else:
                mon_fichier.write(json.dumps(content) + "\n")

    client = bigquery.Client()  # creation d'un nouveau client qui utilise GCP
    dataset_id = "covid_data_esme" 
    table_id = "all_data_covid"
    dataset_ref = client.dataset(dataset_id) #on se connect a la data set puis a la table 
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("pos_7j", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("pos", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("reg_incid_rea", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("incid_dchosp", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("incid_rad", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("incid_rea", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("dchosp", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("cv_dose1", "FLOAT64",mode="NULLABLE"),
            bigquery.SchemaField("incid_hosp", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("rad", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("R", "FLOAT64",mode="NULLABLE"),
            bigquery.SchemaField("rea", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("TO", "FLOAT64",mode="NULLABLE"),
            bigquery.SchemaField("tx_incid", "FLOAT64",mode="NULLABLE"),
            bigquery.SchemaField("tx_pos", "FLOAT64",mode="NULLABLE"),
            bigquery.SchemaField("reg_rea", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("date", "DATE",mode="NULLABLE"),
            bigquery.SchemaField("lib_reg", "STRING",mode="NULLABLE"),
            bigquery.SchemaField("lib_dep", "STRING",mode="NULLABLE"),
            bigquery.SchemaField("reg", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("hosp", "INT64",mode="NULLABLE"),
            bigquery.SchemaField("dep", "INT64",mode="NULLABLE")
        ],
        source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,#on le prend ligne par ligne
        write_disposition = "WRITE_APPEND" #ECRIT EN AJOUTANT
    ) 

    with open(path.join(root, file_path), "rb") as mon_fichier :
        job = client.load_table_from_file (
            mon_fichier,
            table_ref,
            location="europe-west1",
            job_config = job_config
            )
    job.result()
        
    print("Les données ajoutées a la table {}".format(table_ref))




