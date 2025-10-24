# 🎓 Simulateur de Rémunération de Formation

Une application Streamlit interactive pour aider les demandeurs d'emploi à identifier les aides financières disponibles pour leur formation (AREF, RFFT, RFF, etc.).

## 🚀 Démo en ligne

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://votre-app.streamlit.app)

## 📋 Fonctionnalités

- **Simulation interactive** : Répondez à quelques questions pour connaître vos droits
- **Aides couvertes** : AREF, RFF, RFFT, Rémunération Régionale
- **Interface intuitive** : Design moderne et responsive
- **Informations détaillées** : Explications des acronymes et conditions
- **Contacts utiles** : Liens directs vers France Travail et Conseils Régionaux

## 🛠️ Installation locale

### Prérequis
- Python 3.8 ou supérieur
- pip

### Étapes d'installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/votre-username/simulateur-formation.git
   cd simulateur-formation
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'application**
   ```bash
   streamlit run appFormation.py
   ```

4. **Ouvrir dans le navigateur**
   L'application sera accessible à l'adresse : `http://localhost:8501`

## 📱 Utilisation

1. **Répondez aux questions** sur votre situation actuelle
2. **Consultez le résultat** de votre simulation
3. **Explorez les définitions** dans la section d'aide
4. **Suivez les prochaines étapes** recommandées

## 🎯 Types d'aides simulées

### AREF - Allocation d'aide au retour à l'emploi - Formation
- **Bénéficiaires** : Demandeurs d'emploi indemnisés par l'ARE
- **Conditions** : Formation de plus de 40 heures prescrite par France Travail
- **Montant** : Équivalent à l'ARE

### RFF - Rémunération de Fin de Formation
- **Bénéficiaires** : Demandeurs d'emploi dont les droits ARE s'épuisent pendant la formation
- **Conditions** : Période non couverte par l'ARE
- **Montant** : Équivalent à l'ARE

### RFFT - Rémunération de Formation France Travail
- **Bénéficiaires** : Demandeurs d'emploi non indemnisés
- **Conditions** : Formation prescrite par France Travail
- **Montant** : Variable selon la situation (environ 600€/mois)

### Rémunération Régionale
- **Bénéficiaires** : Demandeurs d'emploi suivant une formation régionale
- **Conditions** : Formation financée par la Région
- **Montant** : Variable selon la région

## 🚀 Déploiement sur Streamlit Cloud

### Méthode 1 : Déploiement automatique depuis GitHub

1. **Publiez votre code sur GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connectez-vous à [Streamlit Cloud](https://share.streamlit.io/)**

3. **Cliquez sur "New app"**

4. **Configurez votre app** :
   - **Repository** : `votre-username/simulateur-formation`
   - **Branch** : `main`
   - **Main file path** : `appFormation.py`

5. **Cliquez sur "Deploy!"**

### Méthode 2 : Déploiement manuel

1. **Créez un compte sur Streamlit Cloud**
2. **Importez votre repository GitHub**
3. **Configurez les paramètres de déploiement**
4. **Lancez le déploiement**

## 📁 Structure du projet

```
simulateur-formation/
├── appFormation.py          # Application principale
├── requirements.txt         # Dépendances Python
├── .streamlit/
│   └── config.toml         # Configuration Streamlit
├── .gitignore              # Fichiers à ignorer par Git
└── README.md               # Documentation
```

## 🔧 Configuration

Le fichier `.streamlit/config.toml` contient la configuration de l'application :
- Thème personnalisé
- Paramètres serveur
- Configuration du navigateur

## 📞 Support et contacts

- **France Travail** : 3949 (numéro non surtaxé)
- **Site web** : [france-travail.fr](https://www.france-travail.fr)
- **Conseil Régional** : Vérifiez le numéro de votre région

## ⚠️ Avertissement

Cette application est à but informatif uniquement. Les règles peuvent varier selon votre région ou votre situation personnelle. Consultez toujours votre conseiller France Travail ou votre Conseil Régional pour des informations officielles.

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Soumettre des pull requests

## 📊 Statistiques

![GitHub stars](https://img.shields.io/github/stars/votre-username/simulateur-formation?style=social)
![GitHub forks](https://img.shields.io/github/forks/votre-username/simulateur-formation?style=social)
![GitHub issues](https://img.shields.io/github/issues/votre-username/simulateur-formation)
![GitHub license](https://img.shields.io/github/license/votre-username/simulateur-formation)

---

**Développé avec ❤️ pour aider les demandeurs d'emploi dans leur parcours de formation**