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
        'Get Help': 'https://www.francetravail.fr',
        'Report a bug': "https://github.com/AdeolaRo/orientation-professionnelle/issues",
        'About': "Simulateur d'aides à la formation - Version 2.0"
    }
)

# -----------------------------
# MÉTADONNÉES DE L'APPLICATION
# -----------------------------
APP_VERSION = "2.0.0"
LAST_UPDATE = "2025-10-24"

# -----------------------------
# STYLES CSS PERSONNALISÉS
# -----------------------------
st.markdown("""
<style>
    /* HEADER PRINCIPAL */
    .main-header {
        background: linear-gradient(135deg, #1f4e79, #2e7d32);
        padding: 1.8rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: 0.3s ease;
    }
    .main-header:hover {
        transform: scale(1.01);
    }
    .main-header h1 {
        font-size: 2rem;
        margin-bottom: 0.3rem;
    }

    /* BOÎTES D'INFORMATION */
    .info-box, .success-box, .warning-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-size: 1rem;
    }
    .info-box {
        background-color: #e3f2fd;
        border-left: 5px solid #2196f3;
    }
    .success-box {
        background-color: #e8f5e8;
        border-left: 5px solid #4caf50;
    }
    .warning-box {
        background-color: #fff3e0;
        border-left: 5px solid #ff9800;
    }

    /* BOUTON PRINCIPAL */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #1976d2, #43a047);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #43a047, #1976d2);
        transform: scale(1.02);
    }

    /* EXPANDER STYLE */
    .streamlit-expanderHeader {
        font-weight: 600 !important;
        color: #1f4e79 !important;
    }

    /* RÉPONSIVE */
    @media (max-width: 768px) {
        .main-header h1 { font-size: 1.6rem; }
        .main-header h3 { font-size: 1.1rem; }
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# EN-TÊTE
# -----------------------------
st.markdown("""
<div class="main-header">
    <h1>🎓 Simulation d’Aides à la Formation & Financement </h1>
    <h3>France Travail & Région</h3>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# INTRODUCTION
# -----------------------------
st.markdown("""
<div class="info-box">
    <h4>👋 Bienvenue !</h4>
    <p>Répondez à quelques questions, puis cliquez sur <b>"🔍 Lancer la simulation"</b> pour découvrir vos <strong>droits à la rémunération</strong> pendant la formation (AREF, RFFT, RFF, etc.).</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# BARRE LATÉRALE
# -----------------------------
with st.sidebar:
    st.markdown("### 🏛️ France Travail")
    st.markdown("---")
    st.markdown("### 📞 Contacts utiles")
    st.markdown("""
    **France Travail**  
    📞 3949 (appel non surtaxé)  
    🌐 [francetravail.fr](https://www.francetravail.fr)
    
    **Conseil Régional**  
    🔍 Consultez le site web de votre région pour les dispositifs régionaux.
    """)
    st.markdown("### 📋 Documents utiles")
    st.markdown("""
    - Attestation France Travail  
    - Contrat de formation  
    - RIB  
    - Justificatif de ressources  
    - Pièce d'identité
    """)

# -----------------------------
# QUESTIONS UTILISATEUR
# -----------------------------
st.markdown("## 🧾 Votre situation")

with st.form("simulation_form"):
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
    submitted = st.form_submit_button("🔍 Lancer la simulation")

# -----------------------------
# AFFICHAGE DES RÉSULTATS APRÈS CLIC
# -----------------------------
if submitted:
    st.balloons()
    st.markdown("## 📋 Résultat de votre simulation")

    with st.expander("📝 Résumé de vos réponses", expanded=True):
        st.markdown(f"""
        - **ARE actuelle** : {are}  
        - **Type de formation** : {formation_type}  
        - **Durée** : {formation_duree}  
        - **Droits ARE** : {droits_fin}
        """)

    # Fonction d'affichage stylé
    def display_result(result_type, message, details=None):
        color_class = {
            "success": "success-box",
            "info": "info-box",
            "warning": "warning-box"
        }.get(result_type, "info-box")

        st.markdown(f"""
        <div class="{color_class}">
            <h4>{message}</h4>
            {f'<p>{details}</p>' if details else ''}
        </div>
        """, unsafe_allow_html=True)

    # LOGIQUE PRINCIPALE
    if are == "Oui":
        if formation_duree == "> 40 heures":
            display_result(
                "success",
                "✅ Vous pouvez bénéficier de l'AREF (Allocation d'aide au retour à l'emploi - Formation)",
                "L'AREF est versée pendant toute la durée de votre formation, sous réserve d'assiduité et de validation de votre projet par France Travail."
            )

            if droits_fin == "Non":
                display_result(
                    "info",
                    "ℹ️ Vos droits ARE ne couvrent pas toute la formation",
                    "Vous pouvez demander la **RFF** (Rémunération de Fin de Formation) pour la période non couverte."
                )
            elif droits_fin == "Je ne sais pas":
                display_result(
                    "warning",
                    "❓ Vérification nécessaire",
                    "Contactez votre conseiller France Travail pour confirmer la durée exacte de vos droits."
                )
        else:
            display_result(
                "warning",
                "⚠️ Formation courte",
                "Les formations de moins de 40 heures ne donnent généralement pas droit à l’AREF. Renseignez-vous sur les aides régionales."
            )
    else:
        if formation_type == "Formation France Travail":
            display_result(
                "success",
                "✅ Vous pouvez demander la RFFT (Rémunération de Formation France Travail)",
                "Elle s’adresse aux demandeurs d’emploi non indemnisés suivant une formation validée par France Travail."
            )
        elif formation_type == "Formation Région (ex : SFER)":
            display_result(
                "info",
                "ℹ️ Formation régionale",
                "Vérifiez auprès de votre **Conseil Régional** : certaines régions proposent une rémunération spécifique (SFER)."
            )
        else:
            display_result(
                "warning",
                "⚠️ Financement requis",
                "Un financement validé par France Travail ou la Région est nécessaire pour percevoir une rémunération."
            )

    st.markdown("---")

    # Étapes suivantes
    st.markdown("### ✅ Prochaines étapes")
    st.markdown("""
    - 💬 **Contactez votre conseiller France Travail** pour confirmer vos droits.  
    - 📝 **Faites la demande de rémunération** (AREF, RFF, RFFT, ou aide régionale).  
    - 🔁 **Actualisez chaque mois** votre situation (en indiquant "en formation").  
    """)

# -----------------------------
# SECTION D'AIDE
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

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption(f"""
🛈 Application simplifiée à but informatif – Version {APP_VERSION}  
📅 Dernière mise à jour : {LAST_UPDATE}  
Les règles peuvent varier selon votre région ou votre situation personnelle.  
Sources : dispositifs France Travail & Régions.
""")
