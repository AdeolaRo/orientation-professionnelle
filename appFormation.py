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
        'About': "Simulateur d'aides à la formation - Version 3.2"
    }
)

APP_VERSION = "3.2.0"
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
    st.markdown("### 🏛️ France Travail")
    st.markdown("---")
    
    # Indicateur de thème
    st.markdown("### 🌓 Mode d'affichage")
    st.markdown("""
    L'application s'adapte automatiquement à votre préférence système :
    - **Mode clair** : Interface claire et lumineuse
    - **Mode sombre** : Interface sombre pour réduire la fatigue oculaire
    
    *Changez votre préférence dans les paramètres de votre système.*
    """)
    
    st.markdown("---")
    st.markdown("### 📞 Contacts utiles")
    st.markdown("""
    **France Travail**  
    📞 3949 (appel non surtaxé)  
    🌐 [france-travail.fr](https://www.france-travail.fr)
    
    **Conseil Régional**  
    🔍 Consultez le site web de votre région pour les dispositifs régionaux.
    """)
    st.markdown("### 📋 Documents utiles")
    st.markdown("""
    - Attestation France Travail  
    - Contrat de formation  
    - RIB et justificatifs  
    - Pièce d'identité
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
        # Popup de résultats
        st.markdown("""
        <div style="
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            z-index: 1000;
            display: flex;
            justify-content: center;
            align-items: center;
        " id="result-popup">
            <div style="
                background: white;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                max-width: 600px;
                width: 90%;
                text-align: center;
                animation: popupSlide 0.5s ease-out;
            ">
                <h2 style="color: #1f4e79; margin-bottom: 1rem;">🎯 Résultat de votre simulation</h2>
                <div id="popup-content"></div>
                <button onclick="closePopup()" style="
                    background: linear-gradient(90deg, #1f4e79, #2e7d32);
                    color: white;
                    border: none;
                    padding: 0.8rem 2rem;
                    border-radius: 8px;
                    font-weight: 600;
                    margin-top: 1.5rem;
                    cursor: pointer;
                    transition: all 0.3s ease;
                " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                    ✅ Fermer et voir les détails
                </button>
            </div>
        </div>
        
        <style>
            @keyframes popupSlide {
                from {
                    opacity: 0;
                    transform: scale(0.8) translateY(-50px);
                }
                to {
                    opacity: 1;
                    transform: scale(1) translateY(0);
                }
            }
            
            .popup-result {
                padding: 1rem;
                border-radius: 10px;
                margin: 1rem 0;
                text-align: left;
            }
            
            .popup-success {
                background: rgba(76, 175, 80, 0.1);
                border-left: 6px solid #4caf50;
                color: #2e7d32;
            }
            
            .popup-info {
                background: rgba(33, 150, 243, 0.1);
                border-left: 6px solid #2196f3;
                color: #1976d2;
            }
            
            .popup-warning {
                background: rgba(255, 152, 0, 0.1);
                border-left: 6px solid #ff9800;
                color: #f57c00;
            }
        </style>
        
        <script>
            function closePopup() {
                document.getElementById('result-popup').style.display = 'none';
            }
            
            // Fermer avec Escape
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') {
                    closePopup();
                }
            });
            
            // Fermer en cliquant à l'extérieur
            document.getElementById('result-popup').addEventListener('click', function(e) {
                if (e.target === this) {
                    closePopup();
                }
            });
        </script>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📋 Résultat de votre simulation")

        def box(type_, message, details=""):
            color = {"success":"success-box","info":"info-box","warning":"warning-box"}[type_]
            popup_class = {"success":"popup-success","info":"popup-info","warning":"popup-warning"}[type_]
            
            # Affichage normal
            st.markdown(f"""
            <div class="{color}">
                <h4>{message}</h4>
                <p>{details}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Contenu pour la popup
            popup_content = f"""
            <div class="popup-result {popup_class}">
                <h3>{message}</h3>
                <p>{details}</p>
            </div>
            """
            
            # Injecter le contenu dans la popup
            st.markdown(f"""
            <script>
                document.getElementById('popup-content').innerHTML = `{popup_content}`;
            </script>
            """, unsafe_allow_html=True)

        if are == "Oui":
            if formation_duree == "> 40 heures":
                box("success", "✅ Vous pouvez bénéficier de l’AREF", 
                    "L'AREF (Allocation d’aide au retour à l’emploi - Formation) est versée pendant la formation, sous conditions d’assiduité.")
                if droits_fin == "Non":
                    box("info", "ℹ️ Vos droits ARE ne couvrent pas toute la formation", 
                        "Vous pouvez demander la RFF (Rémunération de Fin de Formation) pour la période restante.")
                elif droits_fin == "Je ne sais pas":
                    box("warning", "❓ Vérification nécessaire", 
                        "Contactez votre conseiller France Travail pour connaître la durée exacte de vos droits.")
            else:
                box("warning", "⚠️ Formation courte", "Les formations de moins de 40h ne donnent généralement pas droit à l’AREF.")
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
        - 💬 Contactez votre conseiller France Travail  
        - 📝 Déposez votre dossier de rémunération (AREF, RFF, RFFT, etc.)  
        - 🔁 Actualisez mensuellement votre situation (“en formation”)  
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
🛈 Application informative & interactive – Version {APP_VERSION}  
📅 Dernière mise à jour : {LAST_UPDATE}  
Sources : France Travail, Service Public, Ministère du Travail, C2RP, Centre Inffo, CMA Hauts-de-France.
""")
