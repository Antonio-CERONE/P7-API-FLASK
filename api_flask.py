import json
import joblib
import pandas as pd
from flask import Flask, request

# Configuration FLASK SERVER
app = Flask(__name__)
app.config.from_object(__name__)
# app.config['SECRET_KEY'] = 'la_clef_secrete_choisie'

# Echantillon de 250 enregistrements de Clients
data = pd.read_csv('data_sample_target.csv',
                   index_col="SK_ID_CURR",
                   encoding='utf-8')
data.sort_index(ascending=True, inplace=True)
target = data.iloc[:, -1:]

sample = data.drop(columns="TARGET")
list_index_sample = list(sample.index)

clf = joblib.load("lgbm_model_saved.joblib")
score = clf.predict_proba(sample)
type(score)
df_score = pd.DataFrame(score,
                        index=list_index_sample,
                        columns=['0', '1']
                        )


@app.route("/", methods=['GET'])
def accueil():
    return "<h1>Bienvenue sur API FLASK</h1>"


@app.route("/api_data/all", methods=['GET'])
def api_data():
    # Afficher toutes les données d'entrée de l'échantillon sample
    return json.dumps(sample.to_json())


@app.route("/api_proba/all", methods=['GET'])
def proba_credit():
    api_score = df_score
    return json.dumps(api_score.to_json())


@app.route("/api_client/all", methods=['GET'])
def labels():
    api_id = list_index_sample
    return json.dumps(api_id)


@app.route("/api_client/choix_client", methods=['GET'])
def api_id_choix():
    # Verifier si un ID est fourni comme paramètre dans l'URL
    # Si un ID est fourni : affecter cet ID à un variable
    # Si un ID n'est pas fourni : générer un message d'erreur dans le navigateur
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Erreur: Pas d’identifiant fourni. Veuillez spécifier un id pour choisir un Client..."
    return "Vous avez choisi le Client ID " + str(id)


@app.route("/api_data/client_choisi", methods=['GET'])
def api_data_choisi():
    # Verifier si un ID est fourni comme paramètre dans l'URL
    # Si un ID est fourni : affecter cet ID à un variable
    # Si un ID n'est pas fourni : générer un message d'erreur dans le navigateur
    if 'id' in request.args:
        id = int(request.args['id'])
        api_data = sample[sample.index == int(id)]
    else:
        return "Erreur: Pas d’identifiant fourni. Veuillez spécifier un id pour choisir un Client..."
    return json.dumps(api_data.to_json())


@app.route("/api_proba/client_choisi", methods=['GET'])
def proba_credit_choisi():
    # Verifier si un ID est fourni comme paramètre dans l'URL
    # Si un ID est fourni : affecter cet ID à un variable
    # Si un ID n'est pas fourni : générer un message d'erreur dans le navigateur
    if 'id' in request.args:
        id = int(request.args['id'])
        api_score = df_score[df_score.index == int(id)]
    else:
        return "Erreur: Pas d’identifiant fourni. Veuillez spécifier un id pour choisir un Client..."
    return json.dumps(api_score.to_json())


# lancement de l'application
if __name__ == '__main__':
    app.run(debug=False)
