# Point d'entrée principal pour Streamlit Cloud
# Ce fichier redirige vers mini-app.py pour simplifier le déploiement

import subprocess
import sys
import os

# Changer vers le répertoire du script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Lancer l'application Streamlit
if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "streamlit", "run", "mini-app.py"])
