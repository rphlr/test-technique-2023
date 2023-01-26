#!/usr/bin/python3
# -*-coding:UTF-8 -*

import os
import configparser
import sqlite3

from flask import g

class Installation:

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

        # Renvoyer la liste des installations et de leurs propriétaires triée par commune puis par capacité
        cursor = self._bdSqlite.cursor()
        cursor.execute("""
            SELECT installations.id, installations.nom, installations.commune, installations.capacite, 
                installations.anneeInstallation, proprietaires.nom as proprietaire
            FROM installations
            JOIN proprietaires ON installations.idProprietaire = proprietaires.id
            ORDER BY installations.commune, installations.capacite
        """)

        rows = cursor.fetchall()

        for row in rows:
            listeInstallation.append({
                'id': row[0],
                'nom': row[1],
                'commune': row[2],
                'capacite': row[3],
                'anneeInstallation': row[4],
                'Proprietaire': row[5]
            })

        return(listeInstallation)

    def listeParProprietaire(self):
        listeInstallationParProprietaire = list()

        # Renvoyer la liste des installations d'un proprietaire en particulier
        cursor = self._bdSqlite.cursor()
        cursor.execute("""
        SELECT installations.id, installations.nom, installations.commune, installations.capacite, 
                installations.anneeInstallation, proprietaires.nom as proprietaire
            FROM installations
            JOIN proprietaires ON installations.idProprietaire = proprietaires.id
            WHERE installations.idProprietaire = ?
            ORDER BY installations.commune, installations.capacite
        """, self)

        rows = cursor.fetchall()

        for row in rows:
            listeInstallationParProprietaire.append({
                'id': row[0],
                'commune': row[2],
                'capacite': row[3],
                'anneeInstallation': row[4],
                'Proprietaire': row[5]
            })

        return(listeInstallationParProprietaire)

    def creer(self):

        cursor = self._bdSqlite.cursor()
        cursor.execute("""
            INSERT INTO installations(nom,commune,capacite,anneeInstallation,idProprietaire)
            VALUES(?,?,?,?,?)"""
        ), (g.nom, g.commune, g.capacite, g.anneeInstallation, g.idProprietaire)
		
        self._bdSqlite.commit()

        return(retour)