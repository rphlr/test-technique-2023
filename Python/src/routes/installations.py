#!/usr/bin/python3
# -*-coding:UTF-8 -*

from flask import make_response
import configparser
import os
import time
import json

from __main__ import app

from classes.installation import Installation

from flask import request

# Chemin de l'API
pathApi = os.path.dirname(os.path.realpath(__file__))

# Récupération config
configApi = configparser.ConfigParser()
configApi.read(pathApi + '/../../conf/config.ini')

@app.route('/installations', methods=['GET'])
def installationsGet(*args, **kwargs):

    installations = Installation()
    listeInstallations = installations.liste()

    response = make_response(json.dumps(listeInstallations), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response

@app.route('/installations/parProprietaire', methods=['GET'])
def installationsParProprietaireGet(*args, **kwargs):

    # Récupérer l'argument "proprietaire" sous forme d'id et renvoyer les installations correspondantes
    idProprietaire = request.args.get('proprietaire')
    if not idProprietaire:
        response = make_response(json.dumps({
            'error': 'Missing argument'
        }), 400)
#        response.headers["Content-Type"] = "text/json; charset=utf-8"
#        return response
#    else:
    try:
        idProprietaire = str(idProprietaire)
    except ValueError:
        return make_response(json.dumps({
            'error': 'Invalid value for argument'
        }), 400)

    installations = Installation()
    listeInstallationsParProprietaire = installations.listeParProprietaire()

    response = make_response(json.dumps(listeInstallationsParProprietaire), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response

@app.route('/installations', methods=['POST'])
def installationsPost(*args, **kwargs):

    # Récupérer les arguments nécessaires à la création d'une nouvelle installation
    nom = data["nom"]
    commune = data["commune"]
    capacite = data["capacite"]
    anneeInstallation = data["anneeInstallation"]
    idProprietaire = data["idProprietaire"]

    # Le propriétaire doit déjà exister
    proprietaire = Proprietaire()
    listeProprietaires = proprietaire.liste()
    proprietaireExiste = False
    for prop in listeProprietaires:
            proprietaireExiste = True
            break

    return response