"""
Cette url permet de récupérer la donnée de tous les départements à une date précise, 
donc admettons qu'à 2h du matin tous les jours on veuille récupérer la donnée de la veille,
il faut que la date en fin d'url soit la date de la veille.

Je te laisse trouve un moyen d'automatiser ça pour qu'automatiquement ce soit la date d'hier et au bon format "DD-MM-YY".
"""
base_url = "https://coronavirusapifr.herokuapp.com/data/departements-by-date/11-10-2021"

yesterday_date = "..."
final_url = (
    f"https://coronavirusapifr.herokuapp.com/data/departements-by-date/{yesterday_date}"
)
# Ici le f"...{}..." permet de mettre une variable dans une chaine de caractères, très pratique pour les url. Eviter les + pour concaténer !

""" 
Ensuite, tu peux essayer d'utiliser le même code que pour la donnée historique pour écrire le résultat de la donnée de la veille dans un fichier JSON.

Une fois que ce sera fait on sera capable d'ingérer automatiquement la donnée Covid dont on aura besoin pour la suite. 
"""
