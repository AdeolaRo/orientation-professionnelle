# 🚀 Guide de déploiement

## Étapes pour publier sur GitHub et Streamlit Cloud

### 1. Préparation du repository GitHub

```bash
# Initialiser Git (si pas déjà fait)
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "Initial commit: Simulateur de rémunération de formation"

# Créer le repository sur GitHub (via l'interface web)
# Puis ajouter l'origine
git remote add origin https://github.com/VOTRE-USERNAME/simulateur-formation.git

# Pousser vers GitHub
git push -u origin main
```

### 2. Déploiement sur Streamlit Cloud

1. **Aller sur [share.streamlit.io](https://share.streamlit.io/)**
2. **Se connecter avec votre compte GitHub**
3. **Cliquer sur "New app"**
4. **Remplir les informations** :
   - **Repository** : `VOTRE-USERNAME/simulateur-formation`
   - **Branch** : `main`
   - **Main file path** : `appFormation.py`
5. **Cliquer sur "Deploy!"**

### 3. Configuration post-déploiement

- L'URL de votre app sera : `https://VOTRE-USERNAME-simulateur-formation-app-XXXXXX.streamlit.app`
- Mettre à jour le README.md avec la vraie URL
- Tester toutes les fonctionnalités

### 4. Mise à jour du README

N'oubliez pas de remplacer dans le README.md :
- `votre-username` par votre vrai nom d'utilisateur GitHub
- L'URL de démonstration par votre vraie URL Streamlit

### 5. Badges GitHub

Ajoutez ces badges à votre README (remplacez `VOTRE-USERNAME` et `simulateur-formation`) :

```markdown
![GitHub stars](https://img.shields.io/github/stars/VOTRE-USERNAME/simulateur-formation?style=social)
![GitHub forks](https://img.shields.io/github/forks/VOTRE-USERNAME/simulateur-formation?style=social)
![GitHub issues](https://img.shields.io/github/issues/VOTRE-USERNAME/simulateur-formation)
![GitHub license](https://img.shields.io/github/license/VOTRE-USERNAME/simulateur-formation)
```

## ✅ Checklist de déploiement

- [ ] Repository GitHub créé
- [ ] Code poussé sur GitHub
- [ ] App déployée sur Streamlit Cloud
- [ ] URL de démonstration mise à jour
- [ ] README.md personnalisé
- [ ] Tests de fonctionnement effectués
- [ ] Badges GitHub ajoutés

## 🔧 Dépannage

### Problèmes courants

1. **Erreur de déploiement** : Vérifiez que `requirements.txt` est présent
2. **App ne se charge pas** : Vérifiez les logs dans Streamlit Cloud
3. **Styles CSS** : Assurez-vous que le fichier `config.toml` est présent

### Support

- [Documentation Streamlit Cloud](https://docs.streamlit.io/streamlit-community-cloud)
- [GitHub Issues](https://github.com/VOTRE-USERNAME/simulateur-formation/issues)
