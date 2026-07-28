# *******************************************************
# Nom ......... : ex4.3.py
# Rôle ........ : Permet de rechercher une date de naissance dans les premières décimales de pi, de connaître le jour de naissance correspondant et d'effectuer des calculs sur les décimales de pi
# Auteur ...... : Mathéo Costecalde
# Version ..... : V0.1 du 15/07/2026
# Licence ..... : réalisé dans le cadre du cours de Outils collaboratifs
# Usage ....... : python3 ex4.3.py
#********************************************************/

#Importation des bibliothèques nécessaires
import streamlit as st
from datetime import datetime

#Configuration de la page Streamlit
st.set_page_config(page_title="Bonus - Pi et dates", layout="centered")

#Affichage du titre
st.title("Recherche dans les décimales de π")

#Fonction permettant de charger les décimales de Pi depuis un fichier texte
def charger_pi():
    try:
        #Ouverture du fichier contenant les décimales de Pi
        with open("1000000.txt", "r") as fp:
            #Lecture du contenu et suppression des espaces inutiles
            return fp.read().strip()
    #Gestion du cas où le fichier n'existe pas
    except FileNotFoundError:
        st.error("Le fichier 1000000.txt est introuvable.")

#Chargement du premier million de décimales de Pi
pi_million = charger_pi()

#Champ permettant à l'utilisateur d'entrer sa date de naissance
date_naissance = st.text_input("Entres ta date de naissance :", placeholder="Exemple : 15092005", max_chars=8)

#Création d'un bouton pour lancer la recherche
if st.button("Rechercher"):
    #Vérification du format de la date saisie
    if len(date_naissance) != 8 or not date_naissance.isdigit():
         #Affichage d'un message d'avertissement si le format est incorrect
        st.warning("Merci de saisir une date de naissance au format JJMMAAAA.")
    else:
        #Recherche de la date dans les décimales de Pi
        if date_naissance in pi_million:
            #Récupération de la position où la date apparaît
            position = pi_million.find(date_naissance)
            #Affichage du résultat
            st.success(f"Ta date de naissance apparaît dans le premier million de décimales de PI à la position {position}.")
        else:
            #Message si la date n'est pas trouvée
            st.warning("Ta date de naissance n'apparaît pas dans le premier million de décimales de PI.")
    #Conversion de la date saisie
    try:
        #Récupération du jour de la semaine
        date = datetime.strptime(date_naissance, "%d%m%Y")
        # Dictionnaire avec les jours en français
        jour = date.strftime("%A")

        jours_fr = {
            "Monday": "Lundi",
            "Tuesday": "Mardi",
            "Wednesday": "Mercredi",
            "Thursday": "Jeudi",
            "Friday": "Vendredi",
            "Saturday": "Samedi",
            "Sunday": "Dimanche"
        }

         #Affichage du jour de naissance
        st.info(f"Tu es né(e) un {jours_fr[jour]}.")

    #Gestion d'une date invalide
    except ValueError:
         st.error("La date de naissance est invalide.")

#Section pour les calculs sur Pi
st.subheader("Sommes des décimales de π")

#Variable pour la somme des 20 premières décimales
somme20 = 0

#Parcours des 20 premières décimales de Pi
for chiffre in pi_million[2:22]:
    #Ajout de chaque chiffre à la somme
    somme20 = somme20 + int(chiffre)

#Variable pour la somme des 144 premières décimales
somme144 = 0

#Parcours des 144 premières décimales de Pi
for chiffre in pi_million[2:146]:
    #Ajout de chaque chiffre à la somme
    somme144 = somme144 + int(chiffre)

#Affichage des résultats des calculs
st.text(f"Somme des 20 premières décimales de PI : {somme20}")
st.text(f"Somme des 144 premières décimales de PI : {somme144}")

#Comparaison des deux sommes
if somme20 == somme144:
    #Message si les deux valeurs sont égales
    st.success("Les deux sommes sont identiques.")
else:
    #Message si les valeurs sont différentes
    st.info("Les deux sommes sont différentes.")

#Section avec la vidéo sur la somme des nombres naturels
st.subheader("La somme des nombres naturels et -1/12")

st.video("https://www.youtube.com/watch?v=GnZQOb9YNV4")