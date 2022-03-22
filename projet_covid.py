# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 17:58:48 2022

@author: alcje
"""

import pandas as pd
import requests

response = requests.get("https://covid-api.mmediagroup.fr/v1/vaccines?country=France")

response_content = response.json()

content = pd.DataFrame.from_dict(response_content)
print (content)
