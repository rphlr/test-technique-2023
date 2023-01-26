#!/usr/bin/python3
# -*-coding:UTF-8 -*

import os
import configparser

class Proprietaire:

    def __init__(self):
        # Chemin de l'API
        pathApi = os.path.dirname(os.path.realpath(__file__))

        # Récupération config
        configApi = configparser.ConfigParser()
        configApi.read(pathApi + '/../../conf/config.ini')

        self._configApi = configApi

        self._bdSqlite = sqlite3.connect(pathApi + '/../../data/dbInstallations.db')

    def liste(self):
        listeInstallation = list()

        # Renvoyer la liste des proprietaires
        cursor = self._bdSqlite.cursor()
        cursor.execute("""
            SELECT *
            FROM proprietaires"""
        )
        rows = cursor.fetchall()
        for row in rows:
            listeInstallation.append({
                "id": row[0],
                "nom": row[1]
            })
        cursor.close()

        return(listeInstallation)

    def creer(self):

        return(retour)