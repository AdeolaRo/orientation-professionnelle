import streamlit as st
import sys
from datetime import datetime

# ------------------------------------
# CONFIGURATION DE LA PAGE
# ------------------------------------
st.set_page_config(
    page_title="Simulation Rémunération Formation",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.francetravail.fr',
        'Report a bug': "https://github.com/AdeolaRo/orientation-professionnelle/issues",
        'About': "Simulateur d'aides à la formation - Version 3.3"
    }
)

APP_VERSION = "3.3.0"
LAST_UPDATE = "2025-10-24"

# ------------------------------------
# STYLES CSS AVEC MODE SOMBRE/CLAIR
# ------------------------------------
st.markdown("""
<style>
    /* Variables CSS pour les thèmes */
    :root {
        --primary-color: #1f4e79;
        --secondary-color: #2e7d32;
        --success-color: #4caf50;
        --info-color: #2196f3;
        --warning-color: #ff9800;
        --text-color: #262730;
        --bg-color: #ffffff;
        --card-bg: #f8f9fa;
        --border-color: #e0e0e0;
    }
    
    /* Mode sombre */
    @media (prefers-color-scheme: dark) {
        :root {
            --text-color: #f0f0f0;
            --bg-color: #0e1117;
            --card-bg: #262730;
            --border-color: #3a3a3a;
        }
    }
    
    /* Mode sombre forcé par l'utilisateur */
    .dark-theme {
        --text-color: #f0f0f0 !important;
        --bg-color: #0e1117 !important;
        --card-bg: #262730 !important;
        --border-color: #3a3a3a !important;
    }
    
    /* Mode clair forcé par l'utilisateur */
    .light-theme {
        --text-color: #262730 !important;
        --bg-color: #ffffff !important;
        --card-bg: #f8f9fa !important;
        --border-color: #e0e0e0 !important;
    }
    
    /* Header principal */
    .main-header {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
        transition: all 0.3s ease;
    }
    
    /* Boîtes d'information adaptatives */
    .info-box, .success-box, .warning-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        transition: all 0.3s ease;
        border: 1px solid var(--border-color);
    }
    
    .info-box { 
        background: rgba(33, 150, 243, 0.1); 
        border-left: 6px solid var(--info-color);
        color: var(--text-color);
    }
    
    .success-box { 
        background: rgba(76, 175, 80, 0.1); 
        border-left: 6px solid var(--success-color);
        color: var(--text-color);
    }
    
    .warning-box { 
        background: rgba(255, 152, 0, 0.1); 
        border-left: 6px solid var(--warning-color);
        color: var(--text-color);
    }
    
    /* Boutons adaptatifs */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        color: white; 
        border: none;
        padding: 0.7rem 2rem; 
        border-radius: 8px;
        font-weight: 600; 
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    div.stButton > button:hover {
        background: linear-gradient(90deg, var(--secondary-color), var(--primary-color));
        transform: scale(1.03);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Onglets adaptatifs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: var(--card-bg);
        color: var(--text-color);
        border-radius: 8px 8px 0 0;
        transition: all 0.3s ease;
        gap: 60px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: var(--primary-color);
        color: white;
    }
    
    /* Sidebar adaptative */
    .css-1d391kg {
        background-color: var(--card-bg);
    }
    
    /* Formulaires adaptatifs */
    .stSelectbox > div > div {
        background-color: var(--card-bg);
        color: var(--text-color);
    }
    
    .stRadio > div {
        background-color: var(--card-bg);
        color: var(--text-color);
    }
    
    /* Expander adaptatif */
    .streamlit-expanderHeader {
        background-color: var(--card-bg);
        color: var(--text-color);
    }
    
    /* Animation de transition globale */
    * {
        transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
    }
    
    /* Indicateur de thème */
    .theme-indicator {
        position: fixed;
        top: 10px;
        right: 10px;
        background: var(--primary-color);
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 12px;
        z-index: 1000;
        opacity: 0.7;
    }
</style>

<script>
    // Appliquer le thème sélectionné
    function applyTheme(theme) {
        const body = document.body;
        body.classList.remove('light-theme', 'dark-theme');
        body.classList.add(theme + '-theme');
    }
    
    // Appliquer le thème au chargement
    document.addEventListener('DOMContentLoaded', function() {
        // Le thème sera appliqué via Streamlit
    });
</script>
""", unsafe_allow_html=True)

# ------------------------------------
# EN-TÊTE
# ------------------------------------
st.markdown("""
<div class="main-header">
    <h1>🎓 Simulation & Informations – Aides à la Formation</h1>
    <h3>France Travail • Régions • Dispositif SFER</h3>
</div>
""", unsafe_allow_html=True)

# ------------------------------------
# BARRE LATÉRALE
# ------------------------------------
with st.sidebar:
    st.markdown(
        "<h3 style='text-align: center;'><b>France Travail</b></h3>", 
        unsafe_allow_html=True)
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
    - Contrat de formation  
    - RIB et justificatifs  
    - Pièce d'identité
    """)
    
    st.markdown("---")
    st.markdown("### 🔒 Sécurisation de la Formation")
    st.markdown("""
    **Étapes recommandées :**
    
    1️⃣ **Définir le projet de formation**
    - Identifier vos compétences
    - Définir vos projet d'évolution professionnel
    
    2️⃣ **Réaliser l'enquête métier**
    - Analyser le marché de l'emploi pour le métier recherché
    - Identifier les débouchés
    
    3️⃣ **Faire une immersion**
    - Découvrir le métier en pratique
        Grace à l'Immerssion facilité 
        https://immersion-facile.beta.gouv.fr/accueil-beneficiaires
    - Réaliser votre immersion pour valider votre choix
    
    4️⃣ **Préparer un CV**
    - Mettre en valeur vos compétences
    - Adapter votre CV au secteur visé
    
    5️⃣ **Préparer une lettre de motivation**
     Expliquer son projet en montrant sa motivation
    """)

# ------------------------------------
# ONGLET PRINCIPAL
# ------------------------------------
tabs = st.tabs([
    "🎯 Simulation de rémunération",
    "📘 Formations (France Travail & Région)",
    "💶 Rémunérations pendant / après formation",
    "🌍 Dispositif SFER (Hauts-de-France)"
])

# ====================================
# ONGLET 1 : SIMULATEUR
# ====================================
with tabs[0]:
    st.markdown("## 🧭 Simulation personnalisée")

    with st.form("simulation_form"):
        are = st.radio("Percevez-vous actuellement l’ARE (Allocation chômage) ?", ["Oui", "Non"])
        formation_type = st.selectbox(
            "Type de formation envisagée :",
            ["Formation France Travail", "Formation Région (ex : SFER)"]
        )
        formation_duree = st.radio("Durée de la formation :", ["> 40 heures", "≤ 40 heures"])
        droits_fin = st.radio("Vos droits ARE couvrent-ils toute la durée de la formation ?", ["Oui", "Non", "Je ne sais pas"])
        submitted = st.form_submit_button("🔍 Lancer la simulation")

    if submitted:
        # Popup de résultats avec Streamlit natif
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #1f4e79, #2e7d32);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            animation: slideIn 0.5s ease-out;
        ">
            <h2 style="margin-bottom: 1rem; font-size: 1.8rem;">🎯 Résultat de votre simulation</h2>
        </div>
        
        <style>
            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateY(-30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📋 Détails de votre simulation")

        def box(type_, message, details=""):
            color = {"success":"success-box","info":"info-box","warning":"warning-box"}[type_]
            
            # Affichage normal
            st.markdown(f"""
            <div class="{color}">
                <h4>{message}</h4>
                <p>{details}</p>
            </div>
            """, unsafe_allow_html=True)
            
            return message, details

        # Déterminer le résultat principal
        main_result = ""
        main_details = ""
        
        if are == "Oui":
            if formation_duree == "> 40 heures":
                main_result = "✅ Vous pouvez bénéficier de l'AREF"
                main_details = "L'AREF (Allocation d'aide au retour à l'emploi - Formation) est versée pendant la formation, sous conditions d'assiduité."
            else:
                main_result = "⚠️ Formation courte"
                main_details = "Les formations de moins de 40h ne donnent généralement pas droit à l'AREF."
        else:
            if formation_type == "Formation France Travail":
                main_result = "✅ Vous pouvez demander la RFFT"
                main_details = "Rémunération de Formation France Travail, pour les non-indemnisés suivant une formation agréée."
            elif formation_type == "Formation Région (ex : SFER)":
                main_result = "ℹ️ Formation régionale"
                main_details = "Vérifiez auprès de votre Conseil Régional : une rémunération régionale peut être disponible."
            else:
                main_result = "⚠️ Financement requis"
                main_details = "Une validation par France Travail ou la Région est obligatoire pour obtenir une rémunération."
        
        # Afficher le résultat principal dans l'en-tête
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #1f4e79, #2e7d32);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            animation: slideIn 0.5s ease-out;
        ">
            <h2 style="margin-bottom: 1rem; font-size: 1.8rem;">🎯 Résultat de votre simulation</h2>
            <h3 style="margin-bottom: 0.5rem; font-size: 1.3rem;">{main_result}</h3>
            <p style="font-size: 1rem; opacity: 0.9;">{main_details}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Afficher les détails complets
        if are == "Oui":
            if formation_duree == "> 40 heures":
                box("success", "✅ Vous pouvez bénéficier de l'AREF", 
                    "L'AREF (Allocation d'aide au retour à l'emploi - Formation) est versée pendant la formation, sous conditions d'assiduité.")
                if droits_fin == "Non":
                    box("info", "ℹ️ Vos droits ARE ne couvrent pas toute la formation", 
                        "Vous pouvez demander la RFF (Rémunération de Fin de Formation) pour la période restante.")
                elif droits_fin == "Je ne sais pas":
                    box("warning", "❓ Vérification nécessaire", 
                        "Contactez votre conseiller France Travail pour connaître la durée exacte de vos droits.")
            else:
                box("warning", "⚠️ Formation courte", "Les formations de moins de 40h ne donnent généralement pas droit à l'AREF.")
        else:
            if formation_type == "Formation France Travail":
                box("success", "✅ Vous pouvez demander la RFFT", 
                    "Rémunération de Formation France Travail, pour les non-indemnisés suivant une formation agréée.")
            elif formation_type == "Formation Région (ex : SFER)":
                box("info", "ℹ️ Formation régionale", 
                    "Vérifiez auprès de votre **Conseil Régional** : une rémunération régionale (stagiaire de la formation professionnelle) peut être disponible.")
            else:
                box("warning", "⚠️ Financement requis", "Une validation par France Travail ou la Région est obligatoire pour obtenir une rémunération.")

        st.markdown("""
        ---
        ### ✅ Prochaines étapes :
        - 💬 Contactez un Organisme de Formation agréé  
        - 📝 Mobiliser votre CPF (en cas de somme insuffisante faire une demande d'abondement aif)
             Sans le CPF demander un devis pour AIF qui sera transmis via ("KAIROS") 
        - 🔁 Actualisez mensuellement votre situation (“en formation”)  

        AIF : Aide Individuel à la Formation.
        """)

# ====================================
# ONGLET 2 : FORMATIONS
# ====================================
with tabs[1]:
    st.markdown("## 🎓 Formations (France Travail & Région)")

    st.markdown("""
    ### 🧍‍♂️ À qui s’adressent-elles ?
    - En tant que demandeur d’emploi, vous pouvez suivre une formation agréée par France Travail.  
    - Les formations peuvent être financées ou co-financées par la **Région** ou l’**État**.  
    - Elles s’inscrivent dans votre **Projet Personnel d’Accès à l’Emploi (PPAE)**.  

    ### 🏗️ Typologie et conditions
    - Formation financée par le **programme régional de formation (PRF)** : inscription via “financée par le Conseil régional”.  
    - Le centre de formation valide vos prérequis, puis votre conseiller France Travail valide le projet.  
    - Une formation doit durer **au moins 40 heures** pour certaines rémunérations.  

    ### 🎯 Objectifs
    - Acquérir de nouvelles compétences, se reconvertir ou renforcer son employabilité.  
    - Souvent orientées vers des **métiers en tension** (via la Région ou France Travail).  
    """)

# ====================================
# ONGLET 3 : RÉMUNÉRATIONS
# ====================================
with tabs[2]:
    st.markdown("## 💶 Rémunérations pendant ou après formation")

    st.markdown("""
    ### Principaux dispositifs :
    - **RFF (Rémunération de Fin de Formation)** : si vos droits ARE/ASP ne couvrent pas toute la durée de la formation.  
    - **RFFT (Rémunération de Formation France Travail)** : pour les non-indemnisés.  
    - **RSFP (Rémunération des Stagiaires de la Formation Professionnelle)** : via la Région ou l’État.  
    - Autres : ARE-F, ASP-F, ATI-F selon situation.

    ### 💰 Montants indicatifs :
    - **RFFT** : de 224,68 € à 769,49 € / mois (jusqu’à 2 170 € pour travailleurs handicapés).  
    - **RFF / R2F** : plafonnée à 652,02 € / mois selon le décret.  
    - **RSFP (Région)** : barème indicatif France Travail  
        - <18 ans : 220,92 €/mois  
        - 18–25 ans : 561,68 €/mois  
        - 26 ans et + : 769,49 €/mois

    ### ⏳ Durée :
    - Les formations doivent durer **≥ 40h**.  
    - RFFT et RFF versées **jusqu’à 3 ans max** pour une même formation.  

    ### 🚗 Autres aides :
    - Aides à la mobilité, hébergement, repas selon situation.  
    - Le versement débute après l’attestation d’entrée en formation.
    """)

# ====================================
# ONGLET 4 : DISPOSITIF SFER
# ====================================
with tabs[3]:
    st.markdown("## 🌍 Dispositif SFER – Se Former pour un Emploi en Région (Hauts-de-France)")

    st.markdown("""
    ### 🎯 Objectif
    Le **SFER** remplace le **Programme Régional de Formation (PRF)**.  
    Il permet aux demandeurs d’emploi d’accéder à des **formations financées à 100% par la Région**.

    ### 👥 Publics concernés
    - Demandeurs d’emploi majeurs inscrits à France Travail.  
    - Salariés en contrat aidé ou à temps partiel (<24h/semaine).  
    - Personnes en reconversion selon les cas.

    ### 🧭 Parcours proposés
    - **Découverte** : définir ou confirmer un projet professionnel.  
    - **Qualifiant** : formation certifiante orientée métier.  
    - **Perfectionnement** : modules courts pour renforcer les compétences.  
    - **Filières d’avenir** : secteurs stratégiques (industrie, électromobilité, bâtiment durable…).

    ### 💶 Financement & rémunération
    - Financement intégral par la **Région Hauts-de-France**.  
    - Gratuit pour le demandeur d’emploi.  
    - Les indemnisés continuent à percevoir leur **ARE** pendant la formation.  
    - Les non-indemnisés peuvent percevoir une **indemnisation ASP**, selon critères.  

    ### 📝 Démarches & conseils
    - Être inscrit à France Travail.  
    - Avoir un projet professionnel validé.  
    - Vérifier que la formation est **labellisée SFER** et financée par la Région.  
    - Respecter l’assiduité et déclarer sa situation chaque mois.
    """)

# ------------------------------------
# PIED DE PAGE
# ------------------------------------
st.markdown("---")
st.caption(f"""
🛈 Application informative - Formation & Rémunération  
📅 Dernière mise à jour : {LAST_UPDATE}  
Sources : France Travail, Service Public, Ministère du Travail, C2RP, Centre Inffo, CMA Hauts-de-France.
""")
