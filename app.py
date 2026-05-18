import streamlit as st

# 1. DONNÉES
catalogue = {
    "Aliments": {
        "Lait": 1.2, "Pain": 0.9, "Nutella": 5.63, "Céréales": 0.7, "Café": 1.4,
        "Chocolat": 3.45, "Thé": 3.3, "Jus de fruit": 1.7, "Soda": 1.10, "Vin": 0.71,
        "Riz": 0.71, "Pâtes": 4.2, "Poisson": 0.71, "Semoule": 2.15, "Huile": 1.15,
        "Vinaigre": 2.15, "Ketchup": 3.5, "Chips": 2.87, "Prince": 6.2, "Steak haché": 15.59,
        "Poulet": 0.89, "Chou-fleur": 0.27, "Poire": 2.61, "Oeufs": 0.61, "Pomme de terre": 0.4
    },
    "Produits Ménagers": {
        "Produit sol": 1.5, "Balai": 3.3, "Aspirateur": 8.7, "Produit vitre": 1.4, "Destop": 2.1,
        "Liquide vaisselle": 2.2, "Serpillère": 1.8, "Gants": 2.1, "Serviette": 1.89, "Chiffon": 1.8,
        "Éponge": 2.2, "Eau de javel": 2.1, "Lessive": 1.78, "Tablette lave-vaisselle": 3.2, "Sac poubelle": 2.98,
        "Papier alu": 2.1, "Torchon": 2.2, "Gel WC": 3.4, "Sceau": 1.92, "Déo Febreze": 2.0
    },
    "Produits de Beauté": {
        "Shampoing": 1.5, "Parfum": 1.0, "Crème": 1.5, "Déodorant": 3.5, "Après rasage": 0.97,
        "Vernis": 16.57, "Rouge à lèvre": 3.5, "Gel coiffant": 2.6, "Dentifrice": 3.6, "Papier toilette": 2.5,
        "Bain de bouche": 1.53, "Brosse à dents": 1.5, "Labello": 1.3, "Pansements": 3.9
    }
}

# Initialisation des variables de session (pour garder le panier en mémoire)
if 'panier' not in st.session_state:
    st.session_state.panier = []
if 'total_carbone' not in st.session_state:
    st.session_state.total_carbone = 0.0

# 2. INTERFACE WEB
st.set_page_config(page_title="Ticket Carbone", page_icon="🌱", layout="centered")

st.title("🌱 Mon Ticket Carbone")
st.caption("Programme réalisé par les élèves de CIEL & MELEC - Lycée Claude Chappe")

# Zone d'ajout
st.subheader("Ajouter un produit")
categorie = st.selectbox("Catégorie :", list(catalogue.keys()))
article = st.selectbox("Produit :", list(catalogue[categorie].keys()))
quantite = st.number_input("Quantité :", min_value=1, max_value=100, value=1)

col1, col2 = st.columns(2)
with col1:
    if st.button("Ajouter au panier 🛒", use_container_width=True):
        cout_unitaire = catalogue[categorie][article]
        cout_total_article = cout_unitaire * quantite
        st.session_state.total_carbone += cout_total_article
        
        texte_liste = f"{quantite}x {article} ({cout_total_article:.2f} kg CO2)"
        st.session_state.panier.append(texte_liste)
        st.rerun()

with col2:
    if st.button("Vider le panier 🗑️", use_container_width=True):
        st.session_state.panier = []
        st.session_state.total_carbone = 0.0
        st.rerun()

# Zone du panier
st.subheader("Votre Panier :")
if st.session_state.panier:
    for item in st.session_state.panier:
        st.text(item)
else:
    st.info("Le panier est vide")

# Résultats
st.divider()
st.metric(label="Taux Carbone Total", value=f"{st.session_state.total_carbone:.2f} kg CO2")

# Équivalences
km_voiture = st.session_state.total_carbone * 4.6
smartphones = st.session_state.total_carbone * 125
jours_arbre = st.session_state.total_carbone * 14.6

st.write("### 🌍 Ce qui équivaut environ à :")
st.write(f"🚗 **{km_voiture:.1f} km** roulés en voiture thermique")
st.write(f"📱 **{int(smartphones)}** recharges de smartphone")
st.write(f"🌳 Ce qu'un arbre mettrait **{jours_arbre:.0f} jours** à absorber !")
