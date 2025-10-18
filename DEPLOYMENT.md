# 🚀 Guide de Déploiement - Application d'Orientation Professionnelle

## 📋 Prérequis

- Compte GitHub
- Compte Streamlit Cloud (gratuit)
- Git installé sur votre machine

## 🔧 Étapes de Déploiement

### 1. Initialiser le dépôt Git

```bash
# Dans le répertoire de votre projet
cd /Users/user/Desktop/Présentation

# Initialiser Git
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "Initial commit: Application d'orientation professionnelle"
```

### 2. Créer un dépôt sur GitHub

1. Allez sur [GitHub.com](https://github.com)
2. Cliquez sur "New repository"
3. Nommez votre dépôt : `orientation-professionnelle` (ou le nom de votre choix)
4. Laissez "Public" sélectionné
5. **Ne cochez PAS** "Add a README file"
6. Cliquez sur "Create repository"

### 3. Connecter votre dépôt local à GitHub

```bash
# Ajouter l'origine (remplacez USERNAME par votre nom d'utilisateur GitHub)
git remote add origin https://github.com/USERNAME/orientation-professionnelle.git

# Pousser le code vers GitHub
git branch -M main
git push -u origin main
```

### 4. Déployer sur Streamlit Cloud

1. Allez sur [share.streamlit.io](https://share.streamlit.io)
2. Cliquez sur "Sign in with GitHub"
3. Autorisez Streamlit à accéder à votre compte GitHub
4. Cliquez sur "New app"
5. Remplissez le formulaire :
   - **Repository** : `USERNAME/orientation-professionnelle`
   - **Branch** : `main`
   - **Main file path** : `mini-app.py`
   - **App URL** : `orientation-professionnelle` (ou votre choix)
6. Cliquez sur "Deploy!"

### 5. Configuration avancée (optionnel)

Si vous voulez personnaliser davantage, vous pouvez créer un fichier `streamlit_app.py` qui sera automatiquement détecté par Streamlit Cloud.

## 🌐 Accès à l'application

Une fois déployée, votre application sera accessible à l'adresse :
`https://orientation-professionnelle.streamlit.app`

## 🔄 Mises à jour

Pour mettre à jour votre application :

```bash
# Modifier vos fichiers
# Puis :
git add .
git commit -m "Mise à jour de l'application"
git push origin main
```

Streamlit Cloud redéploiera automatiquement votre application !

## 🛠️ Dépannage

### Problème : L'application ne se lance pas
- Vérifiez que `requirements.txt` contient toutes les dépendances
- Vérifiez que le fichier principal est `mini-app.py`

### Problème : Erreurs d'importation
- Assurez-vous que toutes les dépendances sont dans `requirements.txt`
- Vérifiez que les chemins des fichiers sont corrects

### Problème : Erreurs de caractères
- Tous les caractères spéciaux ont été remplacés par des équivalents ASCII
- L'application devrait fonctionner sans problème

## 📞 Support

Si vous rencontrez des problèmes :
1. Vérifiez les logs sur Streamlit Cloud
2. Consultez la documentation Streamlit
3. Vérifiez que tous les fichiers sont bien poussés sur GitHub
