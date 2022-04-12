# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 17:58:48 2022

@author: alcje
"""


import json

import pandas as pd
import requests

data = pd.read_csv("departements-france.csv")
# print(data['nom_departement'])

with open("data_full.json", "w") as mon_fichier:
    # num_dep = int(input("choisir un numero de departement"))
    region = data["nom_departement"].tolist()
    dep_a_eviter = ["Corse-du-Sud", "Haute-Corse"]
    for r in region:
        if r is not dep_a_eviter:
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
