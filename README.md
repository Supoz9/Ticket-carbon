# 🌱 Ticket Carbon - Évaluez l'impact écologique de vos achats

**Ticket Carbon** est une application web interactive développée en Python avec **Streamlit**. Co-réalisé et utilisé par les élèves des sections **CIEL** (Cybersécurité, Informatique, Électronique) et **MELEC** (Métiers de l'Électricité) du **Lycée Professionnel Claude Chappe** (Arnage), ce projet a pour but de sensibiliser les jeunes à l'empreinte carbone de nos choix de consommation quotidiens.

Plutôt que de manipuler des chiffres abstraits, l'application transforme un panier d'achats virtuel (façon ticket de caisse) en équivalences concrètes et parlantes pour les élèves.

---

### ✨ Fonctionnalités clés

* **3 Catégories de produits :** Analyse de l'impact des *Aliments*, des *Produits Ménagers* et des *Produits de Beauté*.
* **Saisie intuitive :** Choix des articles et gestion des quantités avec mise à jour dynamique du panier en mémoire via Streamlit Session State.
* **Calculateur CO2 en temps réel :** Estimation immédiate de l'empreinte carbone globale exprimée en kg $CO_2$.
* **Équivalences impactantes :** Traduction visuelle du score carbone en :
  * 🚗 Kilomètres parcourus en voiture thermique.
  * 📱 Nombre de recharges de smartphones.
  * 🌳 Nombre de jours nécessaires à un arbre pour absorber cette pollution.

---

### 🛠️ Stack Technique

* **Langage :** Python 3.x
* **Framework Web UI :** Streamlit (Interface adaptative et réactive)
* **Données :** Indicateurs d'émissions simplifiés (Les valeurs moyennes des produits de l'application ont été mises à jour en se basant sur les chiffres de l'ADEME).

---

### 💻 Installation et Lancement local

#### 1. Prérequis
Assurez-vous d'avoir Python 3 installé sur votre machine.

#### 2. Clonage du dépôt
```bash
git clone [https://github.com/Supoz9/Ticket-carbon.git](https://github.com/Supoz9/Ticket-carbon.git)
cd Ticket-carbon
```

#### 3. Installation de Streamlit
```Bash

pip install streamlit
```

#### 4. Lancement de l'application
```Bash

streamlit run main.py
```

(Remplacez main.py par le nom de votre fichier script s'il est différent). L'application s'ouvrira automatiquement dans votre navigateur web à l'adresse http://localhost:8501.

---

💡 Pistes pédagogiques pour la classe

Ce projet s'intègre parfaitement dans une démarche de transition écologique (EDD) et peut être exploité de plusieurs manières :

   Atelier Analyse d'habitudes : Demander aux élèves de recréer le panier de courses type de leur foyer ou de leur dernier fast-food, puis d'identifier les "points noirs" carbone.

   Défi Sobriété : Concevoir le panier le plus optimisé possible pour obtenir les équivalences les plus basses (le moins de jours d'absorption d'arbre possible sans jeûner).

   Pédagogie active / Code : Pour les filières technologiques (CIEL/MELEC), ce code constitue une excellente base d'activité pour apprendre la manipulation des dictionnaires Python, la gestion d'interfaces web rapides et les variables d'état avec Streamlit.

🤝 Communs Numériques & Partage

Ce projet est open-source et s'inscrit dans la dynamique des outils numériques souverains pour l'éducation.
N'hésitez pas à forker le dépôt pour enrichir la base de données de produits ou y ajouter des visuels et graphiques d'analyse !

📬 Contact : Barthélémy Mennock – barthelemy.mennock@ac-nantes.fr
