import streamlit as st
import sys
from datetime import datetime

# -----------------------------
# CONFIGURATION DE LA PAGE
# -----------------------------
st.set_page_config(
    page_title="Simulation Rémunération Formation",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.france-travail.fr',
        'Report a bug': "https://github.com/votre-username/simulateur-formation/issues",
        'About': "Simulateur d'aides à la formation - Version 1.0"
    }
)

# -----------------------------
# MÉTADONNÉES DE L'APPLICATION
# -----------------------------
APP_VERSION = "1.0.0"
LAST_UPDATE = "2024-01-15"

# -----------------------------
# STYLES CSS PERSONNALISÉS
# -----------------------------
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f4e79, #2e7d32);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #e8f5e8;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4caf50;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ff9800;
        margin: 1rem 0;
    }
    .stRadio > div {
        background-color: #f8f9fa;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.25rem 0;
    }
    .stSelectbox > div > div {
        background-color: #f8f9fa;
        border-radius: 5px;
    }
    @media (max-width: 768px) {
        .main-header {
            padding: 0.5rem;
            margin-bottom: 1rem;
        }
        .main-header h1 {
            font-size: 1.5rem;
        }
        .main-header h3 {
            font-size: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITRES ET INTRODUCTION
# -----------------------------
st.markdown("""
<div class="main-header">
    <h1>🎓 Aide à la rémunération de formation</h1>
    <h3>Demandeurs d'emploi – France Travail & Région</h3>
</div>
""", unsafe_allow_html=True)

st.markdown(
    """
<div class="info-box">
    <h4>👋 Bienvenue dans cet outil de simulation interactif</h4>
    <p>Répondez à quelques questions pour savoir <strong>quelle aide financière</strong> (AREF, RFFT, RFF ou autre) peut s'appliquer à votre formation.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# BARRE LATÉRALE
# -----------------------------
with st.sidebar:
    st.markdown("### 📞 Contacts utiles")
    st.markdown("""
    **France Travail**
    - 📞 3949 (numéro non surtaxé)
    - 🌐 [france-travail.fr](https://www.france-travail.fr)
    
    **Conseil Régional**
    - 📞 Vérifiez le numéro de votre région
    - 🌐 Site web de votre région
    
    **Urgences**
    - 🆘 15 (SAMU)
    - 🚨 17 (Police)
    - 🚒 18 (Pompiers)
    """)
    
    st.markdown("### 📋 Documents à préparer")
    st.markdown("""
    - 📄 Attestation Pôle Emploi
    - 📄 Contrat de formation
    - 📄 Justificatifs de ressources
    - 📄 RIB
    - 📄 Pièce d'identité
    """)

st.markdown("---")

# -----------------------------
# SECTION : QUESTIONS
# -----------------------------
st.markdown("## ➤ Votre situation")

are = st.radio("Percevez-vous actuellement l’ARE (Allocation chômage) ?", ["Oui", "Non"])
formation_type = st.selectbox(
    "Type de formation envisagée :",
    ["Formation France Travail", "Formation Région (ex : SFER)"]
)
formation_duree = st.radio(
    "Durée de la formation :",
    ["> 40 heures", "≤ 40 heures"]
)
droits_fin = st.radio(
    "Vos droits ARE couvrent-ils toute la durée de la formation ?",
    ["Oui", "Non", "Je ne sais pas"]
)

st.markdown("---")

# -----------------------------
# SECTION : RÉSULTAT
# -----------------------------
st.markdown("## 📋 Résultat de votre simulation")

# Validation des réponses
if not are or not formation_type or not formation_duree or not droits_fin:
    st.error("⚠️ Veuillez répondre à toutes les questions pour obtenir votre simulation.")
    st.stop()

# Affichage du résumé des réponses
with st.expander("📝 Résumé de vos réponses"):
    st.markdown(f"""
    - **ARE actuelle** : {are}
    - **Type de formation** : {formation_type}
    - **Durée** : {formation_duree}
    - **Droits ARE** : {droits_fin}
    """)

# Fonction pour afficher les résultats avec style
def display_result(result_type, message, details=None):
    if result_type == "success":
        st.markdown(f"""
        <div class="success-box">
            <h4>✅ {message}</h4>
            {f'<p>{details}</p>' if details else ''}
        </div>
        """, unsafe_allow_html=True)
    elif result_type == "info":
        st.markdown(f"""
        <div class="info-box">
            <h4>ℹ️ {message}</h4>
            {f'<p>{details}</p>' if details else ''}
        </div>
        """, unsafe_allow_html=True)
    elif result_type == "warning":
        st.markdown(f"""
        <div class="warning-box">
            <h4>⚠️ {message}</h4>
            {f'<p>{details}</p>' if details else ''}
        </div>
        """, unsafe_allow_html=True)

# Logique principale améliorée
if are == "Oui":
    if formation_duree == "> 40 heures":
        display_result("success", 
                      "Vous pouvez bénéficier de l'**AREF** (Allocation d'aide au retour à l'emploi - Formation)",
                      "L'AREF est versée pendant toute la durée de votre formation, sous réserve de respecter vos obligations.")
        
        if droits_fin == "Non":
            display_result("info",
                          "Vos droits ARE ne couvrent pas toute la formation",
                          "Vous pouvez demander la **RFF** (Rémunération de Fin de Formation) pour la période non couverte par l'ARE.")
        elif droits_fin == "Je ne sais pas":
            display_result("warning",
                          "Vérification nécessaire",
                          "Contactez votre conseiller France Travail pour vérifier la durée exacte de vos droits ARE.")
    else:
        display_result("warning",
                      "Formation de courte durée",
                      "Les formations de moins de 40 heures ne donnent généralement pas droit à l'AREF. Vérifiez les alternatives possibles.")
else:
    if formation_type == "Formation France Travail":
        display_result("success",
                      "Vous pouvez demander la **RFFT** (Rémunération de Formation France Travail)",
                      "La RFFT est versée aux demandeurs d'emploi non indemnisés qui suivent une formation prescrite par France Travail.")
    elif formation_type == "Formation Région (ex : SFER)":
        display_result("info",
                      "Formation régionale",
                      "Vérifiez auprès de votre **Conseil Régional** : une rémunération régionale (stagiaire de la formation professionnelle) peut être disponible selon votre région.")
    else:
        display_result("warning",
                      "Financement requis",
                      "Vous devez disposer d'un financement validé par France Travail ou la Région pour percevoir une rémunération.")

st.markdown("---")

# -----------------------------
# SECTION : PROCHAINES ÉTAPES
# -----------------------------
st.markdown("### ✅ Prochaines étapes")

st.markdown("""
- 💬 **Contactez votre conseiller France Travail** pour valider le projet de formation.  
- 📝 **Déposez votre dossier** de demande de prise en charge et rémunération (AREF, RFF, RFFT…).  
- 🔁 **Actualisez chaque mois** votre situation en indiquant que vous êtes en formation.  
- 📞 En cas de doute, appelez le **3949** (France Travail) ou votre **Conseil Régional**.
""")

st.markdown("---")

# -----------------------------
# SECTION : AIDE ET DÉFINITIONS
# -----------------------------
with st.expander("📚 Aide et définitions des acronymes"):
    st.markdown("""
    ### 🎯 **AREF** - Allocation d'aide au retour à l'emploi - Formation
    - **Qui** : Demandeurs d'emploi indemnisés par l'ARE
    - **Quand** : Formation de plus de 40 heures prescrite par France Travail
    - **Montant** : Équivalent à l'ARE, versé pendant toute la formation
    - **Conditions** : Respecter les obligations (assiduité, recherche d'emploi...)
    
    ### 💰 **RFF** - Rémunération de Fin de Formation
    - **Qui** : Demandeurs d'emploi dont les droits ARE s'épuisent pendant la formation
    - **Quand** : Période non couverte par l'ARE
    - **Montant** : Équivalent à l'ARE
    - **Durée** : Jusqu'à la fin de la formation
    
    ### 🏢 **RFFT** - Rémunération de Formation France Travail
    - **Qui** : Demandeurs d'emploi non indemnisés
    - **Quand** : Formation prescrite par France Travail
    - **Montant** : Variable selon la situation (environ 600€/mois)
    - **Conditions** : Formation de plus de 120 heures
    
    ### 🌍 **Rémunération Régionale**
    - **Qui** : Demandeurs d'emploi suivant une formation régionale
    - **Quand** : Formation financée par la Région (ex: SFER)
    - **Montant** : Variable selon la région
    - **Conditions** : Vérifier auprès de votre Conseil Régional
    """)

st.markdown("---")

# -----------------------------
# SECTION : À PROPOS
# -----------------------------
# -----------------------------
# FOOTER AVEC MÉTADONNÉES
# -----------------------------
st.markdown("---")
st.caption(f"""
🛈 Application simplifiée à but informatif - Version {APP_VERSION} | Dernière mise à jour : {LAST_UPDATE}  
Les règles peuvent varier selon votre région ou votre situation personnelle.  
Source : dispositifs France Travail et Régions.
""")

# -----------------------------
# INFORMATIONS TECHNIQUES (CACHÉES)
# -----------------------------
with st.expander("🔧 Informations techniques", expanded=False):
    st.code(f"""
    Version de l'application : {APP_VERSION}
    Python version : {sys.version.split()[0]}
    Streamlit version : {st.__version__}
    Dernière mise à jour : {LAST_UPDATE}
    """)
