#!/bin/bash

# Script pour lancer l'application Streamlit
# Assurez-vous d'être dans le bon répertoire

echo "🚀 Lancement de l'application Streamlit..."
echo "📁 Répertoire: $(pwd)"

# Vérifier que l'environnement virtuel existe
if [ ! -d "venv" ]; then
    echo "❌ Erreur: L'environnement virtuel 'venv' n'existe pas"
    echo "💡 Créez-le avec: python3 -m venv venv"
    exit 1
fi

echo "🐍 Activation de l'environnement virtuel..."

# Activer l'environnement virtuel
source venv/bin/activate

echo "✅ Environnement virtuel activé"

# Vérifier que Streamlit est installé
if ! python -c "import streamlit" 2>/dev/null; then
    echo "❌ Erreur: Streamlit n'est pas installé"
    echo "💡 Installez-le avec: pip install streamlit pandas"
    exit 1
fi

echo "🌐 Lancement de l'application sur http://localhost:8501"
echo "⏹️  Appuyez sur Ctrl+C pour arrêter l'application"
echo ""

# Lancer Streamlit
streamlit run mini-app.py
