import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
csv=pd.read_csv(r"C:\Users\viole\Documents\Exercices\S11\Quête 1.3 Streamlit\identification.csv")

utilisateurs = {"usernames": {}}

for i in range(len(csv)):
    username = csv["name"][i]

    utilisateurs["usernames"][username] = {
        "email": csv["email"][i],
        "name": csv["name"][i],
        "password": str(csv["password"][i]),
        "role": csv["role"][i],
        "failed_login_attempts": 0,
        "logged_in": False
    }

authenticator = Authenticate(
    utilisateurs,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)
authenticator.login()

def accueil():
      st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")
if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')

# On affiche un menu déroulant (selectbox) DANS la barre latérale (sidebar)
# L'utilisateur peut choisir son moyen de contact préféré parmi trois options
# Autre façon d'utiliser la sidebar avec un "with", pour grouper plusieurs éléments
with st.sidebar:
    # On affiche des boutons radio dans la sidebar pour choisir un mode de livraison
    st.write("Bienvenue " + username)
    st.button("Déconnexion")

    # Création du menu qui va afficher les choix qui se trouvent dans la variable options
    selection = option_menu(
            menu_title=None,
            options = ["Accueil 🏠", "Photos 📷"]
        )
# On indique au programme quoi faire en fonction du choix
if selection == "Accueil 🏠":
    st.write("Bienvenue sur la page d'accueil !")
elif selection == "Photos 📷":
# Création de 3 colonnes 
    col1, col2, col3 = st.columns(3)

# Contenu de la première colonne : 
    with col1:
        st.header("Je vous présente Loukoum!")
        st.image(r"C:\Users\viole\Downloads\IMG-20231128-WA0016.jpg")
#Contenu de la deuxième colonne :
    with col2:
        st.header("Encore Loukoum")
        st.image(r"C:\Users\viole\Downloads\20231204_113414.jpg")
        st.write(" C'est un basset artésien normand. Elle est très gentille, un peu bête (chut! faut pas lui dire!), et très têtue")

# Contenu de la troisième colonne : 
    with col3:
        st.header("Et voilà Vasco!")
        st.image(r"C:\Users\viole\Downloads\20240823_205643.jpg")
        st.write(" Il vient d'avoir 1 an!C'est un basset fauve de Bretagne. C'est pas un grand chien mais il est super vif. Il veut tout le temps jouer. Il est beaucoup plus fût-fût que sa soeur")
# ... et ainsi de suite pour les autres pages