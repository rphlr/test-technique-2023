==============================================================================
                           TEST TECHNIQUE PRÉALABLE
                                 Genedis
                                                                  Janvier 2023
==============================================================================

Bonjour,

Vous trouverez dans cette archive deux ébauches de projets destinés à évaluer
en quelques lignes vos aptitudes pour le poste de développeur PHP / Python.

Le test n'a pas pour vocation à être exhaustif sur vos connaissances, mais à
évaluer vos capacités, votre façon de faire et les réflexions que vous
pourriez apporter sur ce type de projet.

L'ensemble des développements demandés ne devrait pas vous prendre plus d'une
demi journée (plus que de finir le projet lui-même, nous sommes intéressés 
à voir comment vous traitez chacune des problématiques), et lors de 
l'évaluation de multiples critères seront pris en compte : traitement de la 
demande, lisibilité et esthétique du code, ajouts personnels et optimisations,
esthétique du rendu final, ...

N'hésitez pas à nous contacter en cas d'incompréhension dans l'énoncé.

------------------------------------------------------------------------------
                                   Contexte
------------------------------------------------------------------------------

Un collaborateur a démarré un nouveau projet de visualisation du nombre
d'installations photovoltaïque. Rapidement appelé à d'autres tâches, ce
dernier n'a pas pu terminer le projet et l'a laissé en l'état, incomplet et
avec plusieurs erreurs.
Votre tâche est de corriger l'existant et de compléter les fonctions
existantes.

Une base de données SQLite déjà garnie est fournie. Elle est composée des
tables suivantes :
 - installations
  - id (int)
  - nom (varchar 32)
  - commune (text)
  - capacite (float)
  - anneeInstallation (text)
  - idProprietaire (int)
 - proprietaires
  - id (int)
  - nom (varchar 32)
Il est inutile de modifier la structure de cette base de données.


------------------------------------------------------------------------------
                                  Consigne
------------------------------------------------------------------------------

L'API REST en Python doit être complétée (les fonctions attendues sont déjà
créées), et l'interface de visualisation doit afficher sous forme textuelle
et graphique les données de la base SQLite via l'API exclusivement.
Une ébauche du dashboard de visualisation est fournie avec quelques images
en guise de démonstration. Elle mérite d'être complétée et largement améliorée
graphiquement.


------------------------------------------------------------------------------
                 Détails concernant la partie PHP/HTML/Javascript
------------------------------------------------------------------------------

L'installation d'un serveur de type WAMP/LAMP sur votre poste ou une machine
virtuelle ou via Docker est de votre ressort.

Votre code devra être compatible PHP 7 ou 8. S'il y a des spécificités pour
exécuter le serveur ou lancer le code, merci de nous les indiquer.
L'utilisation d'un framework PHP est facultative. Si vous souhaitez en
utiliser un, seul Laravel pourra l'être. 
Le choix de la librairie graphique pour les graphes est libre. Elle doit 
cependant être open-source.
Afin d'être cohérent avec les autres projets que nous développons, la
librairie JS à utiliser est jQuery. Bootstrap peut également être utilisé.
Les autres frameworks comme React, AngluarJS, Vue.js ne peuvent
pas être utilisés pour ce test.


------------------------------------------------------------------------------
                     Détails concernant la partie Python
------------------------------------------------------------------------------

Votre code devra être compatible Python 3 et la structure d'origine devrait
être conservée. Si ce n'est pas le cas, attendez-vous à devoir le justifier :)

La base SQLite se trouve à l'emplacement data/dbInstallations.db


------------------------------------------------------------------------------
                                   Rendu
------------------------------------------------------------------------------

L'ensemble des développements doit être transmis dans un fichier .zip en
conservant la structure du .zip initial. Ce fichier doit être joint à la
réponse au mail que vous avez reçu.
Vous pouvez également déposer votre code sur un dépôt public et nous
transmettre un lien pour y accéder.

N'hésitez pas à nous faire part de vos commentaires et de tout ce que vous
jugeriez utile de préciser.

Bonne chance !
