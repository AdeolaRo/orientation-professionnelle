# 🎯 Application d'Orientation Professionnelle

Application web interactive pour l'évaluation des compétences et l'orientation métier.

## 🌐 Déploiement en ligne

**Application déployée :** [Lien vers votre application](https://votre-app.streamlit.app)

## 📋 Fonctionnalités

1. **Questionnaire interactif** : Évaluation des compétences et préférences
2. **Suggestions de métiers** : Recommandations basées sur les réponses
3. **Plan d'action personnalisé** : Génération de PDF avec recommandations
4. **Présentation PowerPoint** : Support pour les présentations professionnelles

## 🛠️ Outils inclus

- **mini-app-rome.py** : Application web interactive avec données ROME officielles (Streamlit)
- **mini-app.py** : Application web interactive simplifiée (Streamlit)
- **presentation.py** : Générateur de présentation PowerPoint
- **PassActive.py** : Générateur de questionnaire PDF

## Prérequis

- Python 3.6 ou supérieur
- Le fichier `logo.png` doit être présent dans le répertoire

## Installation

1. Cloner ou télécharger ce projet
2. Créer un environnement virtuel :
   ```bash
   python3 -m venv venv
   ```
3. Activer l'environnement virtuel :
   ```bash
   source venv/bin/activate  # Sur macOS/Linux
   # ou
   venv\Scripts\activate     # Sur Windows
   ```
4. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Présentation PowerPoint
1. Assurez-vous que le fichier `logo.png` est présent dans le répertoire
2. Exécutez le script :
   ```bash
   python presentation.py
   ```
3. Le fichier `Projet_Parcours_Competences_Retour_Emploi_CUSTOM.pptx` sera généré

### Questionnaire PDF
1. Exécutez le script :
   ```bash
   python PassActive.py
   ```
2. Le fichier `Questionnaire_Profil_Competences.pdf` sera généré

### Application Web Interactive

#### Version avec données ROME officielles (recommandée)
```bash
source venv/bin/activate
streamlit run mini-app-rome.py
```

#### Version simplifiée
```bash
source venv/bin/activate
streamlit run mini-app.py
```

2. Ouvrez votre navigateur sur http://localhost:8501
3. Utilisez l'interface pour répondre au questionnaire et obtenir des suggestions de métiers

## Contenu de la présentation

La présentation comprend :
- Une slide de titre avec logo
- 10 slides de contenu couvrant :
  - Contexte et enjeux
  - Objectifs
  - Public cible
  - Format et déroulé
  - Contenu par séance
  - Livrables
  - Partenaires mobilisés
  - Indicateurs de réussite
  - Budget prévisionnel
  - Prochaines étapes

## Personnalisation

Vous pouvez modifier :
- Le contenu des slides dans la fonction `main()`
- Les couleurs dans les constantes `TITLE_COLOR` et `TEXT_COLOR`
- La police dans la constante `FONT_NAME`
- Le logo en remplaçant le fichier `logo.png`

## Dépendances

- `python-pptx` : Bibliothèque pour créer et modifier des présentations PowerPoint
- `fpdf2` : Bibliothèque pour générer des fichiers PDF
- `streamlit` : Framework pour créer des applications web interactives
- `pandas` : Bibliothèque pour la manipulation de données
