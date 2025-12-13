# 🤖 Chatbot RAG avec Chainlit, Embeddings et PostgreSQL

Ce projet implémente un **système RAG (Retrieval‑Augmented Generation)** permettant d’améliorer la qualité des réponses générées par un **modèle de langage (LLM)** en intégrant une **recherche sémantique** dans une base de données vectorielle.

L’application utilise **Chainlit** comme interface conversationnelle, un **modèle d’embeddings** pour représenter les textes sous forme vectorielle, et **PostgreSQL + pgvector** pour stocker et interroger efficacement ces vecteurs.

---

## 🧠 Objectif du projet

L’objectif principal est de construire un assistant intelligent capable de :

* Convertir un message utilisateur en **vecteur embedding**
* Comparer ce vecteur avec ceux stockés dans la base de données
* Récupérer les **documents (chunks) les plus pertinents**
* Fournir ces documents comme **contexte** au LLM
* Générer une réponse **précise, contextualisée et fiable**

Ce pipeline permet au modèle de langage de s’appuyer sur des **données réelles issues d’une base documentaire**, réduisant ainsi les hallucinations.

---

## 🧱 Architecture du système

L’architecture repose sur un **pipeline Traditional RAG**, simple et linéaire.

### 📌 Vue d’ensemble

```text
Utilisateur → Chainlit → Embedding requête → Recherche vectorielle (PostgreSQL)
           → Chunks pertinents → LLM → Réponse → Chainlit
```

### 🖼️ Schéma de l’architecture

*(Ajouter l’image de l’architecture dans le dépôt, par exemple : `docs/architecture.png`)*

```md
![Architecture RAG](docs/architecture.png)
```

---

## 🔍 Description détaillée de l’architecture

### 1️⃣ Interface utilisateur – Chainlit

* L’utilisateur saisit une question en **langage naturel**.
* Chainlit assure :

  * La gestion de la conversation
  * L’envoi de la requête au backend
  * L’affichage de la réponse finale

👉 **Valeur ajoutée** : interaction simple et fluide avec le système RAG.

---

### 2️⃣ Vectorisation de la requête utilisateur

* La question est transformée en **embedding** via un modèle d’embeddings.
* Ce vecteur capture la **signification sémantique** du message.



---

### 3️⃣ Base de données PostgreSQL + pgvector

* La base contient :

  * Des **documents découpés en chunks**
  * Un **embedding associé à chaque chunk**
* Les embeddings sont pré‑calculés lors de la phase d’ingestion.

👉 **Avantages** :

* Stockage persistant
* Recherche vectorielle efficace
* Intégration simple avec SQL

---

### 4️⃣ Recherche par similarité vectorielle

* L’embedding de la requête est comparé aux embeddings stockés.
* Une mesure de similarité (ex. **cosinus**) est utilisée.
* Les **top‑k chunks** les plus proches sont sélectionnés.

👉 **Rôle clé du RAG** : identifier les documents réellement pertinents.

---

### 5️⃣ Sélection des documents pertinents (chunks)

* Les chunks récupérés constituent le **contexte**.
* Seules les informations utiles sont transmises au LLM.

👉 **Impact** : réduction du bruit et amélioration de la qualité des réponses.

---

### 6️⃣ Modèle de langage (LLM)

* Le LLM reçoit :

  * La question utilisateur
  * Les chunks pertinents
* Il génère une **réponse en langage naturel**, basée sur le contexte fourni.

👉 **Bénéfice** : réponses plus factuelles et contextualisées.

---

### 7️⃣ Génération et affichage de la réponse

* La réponse est renvoyée vers Chainlit.
* Elle est affichée à l’utilisateur dans l’interface.

---

## 🖥️ Technologies utilisées

| Technologie                   | Rôle                                    |
| ----------------------------- | --------------------------------------- |
| Python                        | Backend du projet                       |
| Chainlit                      | Interface conversationnelle             |
| LLM (Llama3.2)                | Génération de texte                     |
| Modèle d’embeddings           | Représentation vectorielle              |
| PostgreSQL + pgvector         | Base de données & recherche vectorielle |

---

## ⚙️ Installation & Exécution

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/votre-nom/rag-chatbot.git
cd rag-chatbot
```

### 2️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```


### 3️⃣ Lancer l’application

```bash
chainlit run chainlit_app/main.py
```

---

## 🚀 Type de RAG implémenté

* ✅ Traditional RAG
* ❌ Agentic RAG
* ❌ Graph RAG

👉 Cette architecture sert de **base solide** pour des évolutions futures.

---

## 🔮 Perspectives d’amélioration

* Ajout d’un **Agentic RAG**
* Intégration d’un **Graph RAG**
* Évaluation automatique des réponses
* Support multimodal (PDF, images, audio)

---

© 2025 – Projet académique RAG
