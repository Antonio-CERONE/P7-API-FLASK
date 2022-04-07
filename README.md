# P07 - Implémenter un Modèle de Credit Scoring → API FLASK


## Contexte du projet
Développement d'un modèle de notation de Crédit à la Consommation qui prédit, pour un Client, la probabilité de rembourser ce crédit et qui permet ainsi de statuer sur l'octroi ou non de ce crédit (i.e. Crédit Accordé ou Crédit Refusé).


## Objectifs 
- **Fournir une API permettant d'extraire les données d'un Client en particulier**
      
   
## Livrables
- API [**Flask**](https://pypi.org/project/Flask/) deployée sous **HEROKU**<br>
      - <u>*Vision globale de tout l'echantillon de données*</u><br>
                  - Vers [**API-Clients**](https://p7-api-flask.herokuapp.com/api_client/all)<br>
                  - Vers [**API-Data**](https://p7-api-flask.herokuapp.com/api_data/all)<br>
                  - Vers [**API-Probabilités**](https://p7-api-flask.herokuapp.com/api_proba/all)<br><p>
      - <u>*Vision locale, pour un Client particulier, ici le Client ID 330086 par exemple..*</u><br>
                  - Vers [**API-Client ID 201224**](https://p7-api-flask.herokuapp.com/api_client/choix_client?id=330086)<br>
                  - Vers [**API-Data-Client ID 201224**](https://p7-api-flask.herokuapp.com/api_data/client_choisi?id=330086)<br>
                  - Vers [**API-Probabilités-Client ID 201224**](https://p7-api-flask.herokuapp.com/api_proba/client_choisi?id=330086)<br>


---
