# 📘 Chatbot RAG avec Chainlit, Embeddings et PostgreSQL

Ce projet implémente un système **RAG (Retrieval-Augmented Generation)** permettant d’améliorer la qualité des réponses générées par un modèle de langage (LLM) en intégrant une recherche sémantique dans une base de données.

L'application utilise **Chainlit** comme interface conversationnelle, un **modèle d’embeddings** pour représenter les textes sous forme vectorielle, et **PostgreSQL + pgvector** pour stocker et interroger efficacement ces vecteurs.

---

## 🧠 Objectif du projet

L’objectif est de construire un **assistant intelligent** capable de :

- Convertir un message utilisateur en **vecteur embedding**
- Comparer ce vecteur avec ceux stockés dans la base de données
- Récupérer les documents les plus pertinents (chunks)
- Fournir ces documents au **LLM**
- Générer une réponse précise et contextualisée

Ce pipeline permet au modèle de s’appuyer sur des données réelles provenant de votre base documentaire.

---

## 🧱 Architecture du système

Le flux général du RAG suit les étapes suivantes :

1. **Message utilisateur** envoyé depuis l’interface Chainlit
2. **Génération d’un embedding** représentant le message utilisateur
3. **Recherche vectorielle** dans PostgreSQL (similitude cosinus / distance)
4. **Récupération des chunks pertinents**
5. Le LLM génère une réponse enrichie par ces documents
6. **Réponse affichée** dans l'interface Chainlit

---

## 🖥️ Technologies utilisées

| Technologie                       | Rôle                                    |
| --------------------------------- | --------------------------------------- |
| **Python**                        | Backend du projet                       |
| **Chainlit**                      | Interface conversationnelle             |
| **LLM** (OpenAI, Llama, Mistral…) | Génération de texte                     |
| **Embeddings**                    | Représentation vectorielle              |
| **PostgreSQL + pgvector**         | Base de données + recherche vectorielle |
| **Docker** (optionnel)            | Conteneurisation                        |



## ⚙️ Installation & exécution

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/votre-nom/rag-chatbot.git
cd rag-chatbot

### 2️⃣ Installer les dépendances
pip install -r requirements.txt

###3️⃣ Configurer PostgreSQL

Activer l’extension pgvector :

Créer une table pour stocker les embeddings :
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding vector(1536)
);
CREATE EXTENSION IF NOT EXISTS vector;

###4️⃣ Lancer l’application
chainlit run chainlit_app/main.py
```
