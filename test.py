#Ouverture d'un fichier CSV
#Création des listes des lignes nommée tableau...
#et affichage des lignes
import csv
with open ('conso-annuelles_v1.csv',newline='') as f: #ouverture du fichier csv
    tableau=[]
    lire=csv.reader(f)                                #Chargement des lignes du fichier csv
    print('',end='\n')
    print('Affichage des lignes du tableau',end='\n')
    for ligne in lire:                                # Pour chaque ligne
        print(ligne, end='\n')                        # afficher la ligne dans la console
        tableau.append(ligne)                         # ajouter la ligne dans la liste
                                                      # liste   nommée tableau
test