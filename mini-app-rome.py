import streamlit as st
import pandas as pd
from fpdf import FPDF
from io import BytesIO
from datetime import date

# ---------------------
# CONFIGURATION PAGE
# ---------------------
st.set_page_config(page_title="Orientation Professionnelle ROME", page_icon="🎯", layout="wide")
st.title("Questionnaire d'Orientation Professionnelle")
st.markdown("**Basé sur les données ROME officielles – Analyse Poussée**")

LAST_UPDATE = date.today().strftime("%d-%m-%Y")

# ---------------------
# CHARGEMENT DONNÉES
# ---------------------
@st.cache_data
def load_rome_data():
    try:
        metiers = pd.read_csv("RefRomeCsv/unix_referentiel_code_rome_v460_utf8.csv")
        competences = pd.read_csv("RefRomeCsv/unix_referentiel_competence_v460_utf8.csv")
        centres = pd.read_csv("RefRomeCsv/unix_centre_interet_v460_utf8.csv")
        correspondances = pd.read_csv("RefRomeCsv/unix_lien_centre_metier.csv")
        return metiers, competences, centres, correspondances
    except Exception as e:
        st.error(f"Erreur chargement ROME : {e}")
        return None, None, None, None

metiers_df, competences_df, centres_interet_df, correspondances_df = load_rome_data()

# ---------------------
# UTILITAIRES
# ---------------------
def get_code_rome_column(df, df_name="DataFrame"):
    if "code_rome" in df.columns:
        return "code_rome"
    elif "Code_Rome" in df.columns:
        return "Code_Rome"
    else:
        st.error(f"❌ La colonne code_rome est introuvable dans {df_name}")
        st.write(f"Colonnes disponibles : {df.columns.tolist()}")
        return None

# ---------------------
# SECTEURS → FAMILLES ROME
# ---------------------
SECTEURS_ROME = {
    "Tous secteurs": [],
    "Informatique / Numérique": ["M18", "I13"],
    "Santé / Social": ["J15", "J14"],
    "Commerce / Vente": ["D14", "D15"],
    "Administration / Services": ["M16", "K21"],
    "Transport / Logistique": ["N11", "N12"],
    "Agriculture / Environnement": ["A11", "A12"],
    "Artisanat / BTP": ["F11", "F12"]
}

# ---------------------
# ANALYSE POUSSEE 
# ---------------------
INTENT_MAP = {
    "infirmier": ["J15"], "soigner": ["J15"], "santé": ["J15", "J14"], "médical": ["J15"],
    "aider": ["J15", "J14", "K21"], "accompagner": ["J15", "J14", "K21"], "assistant": ["M16"],
    "coder": ["M18"], "développer": ["M18"], "informatique": ["M18", "I13"], "numérique": ["M18"],
    "réparer": ["I13", "H22"], "installer": ["H22"], "construire": ["F11", "F12"],
    "chantier": ["F12"], "vendre": ["D14", "D15"], "commerce": ["D14", "D15"],
    "conduire": ["N11", "N12"], "livrer": ["N12"], "nature": ["A11", "A12"],
    "agriculture": ["A11"], "bureau": ["M16"], "administration": ["M16"],
    "manager": ["M17"], "diriger": ["M17"], "gérer": ["M17"], "formation": ["K21"],
    "enseigner": ["K21"], "formation continue": ["K21"]
}

def analyse_objectifs_nlp(objectifs):
    if not objectifs:
        return [], []
    text = objectifs.lower()
    keywords = []
    families_detected = []
    
    for mot, familles in INTENT_MAP.items():
        if mot in text:
            keywords.append(mot)
            families_detected.extend(familles)
    
    # Approximation sur premiers caractères pour détecter variantes
    mots_objectifs = text.split()
    for mot_obj in mots_objectifs:
        for mot, familles in INTENT_MAP.items():
            if mot_obj.startswith(mot[:4]):
                if mot not in keywords:
                    keywords.append(mot)
                    families_detected.extend(familles)

    return list(set(families_detected)), keywords

# ---------------------
# MATCHER MÉTIERS
# ---------------------
def matcher_metiers(centres_user, compet_tech, soft_skills, secteur, objectifs):

    df = metiers_df.copy()
    df["score"] = 0

    metiers_code_col = get_code_rome_column(df, "metiers_df")
    if not metiers_code_col:
        return pd.DataFrame(), [], []

    # Centres d'intérêt
    if centres_user:
        centres_codes = [c.split(" - ")[0] for c in centres_user]
        metiers_ci = correspondances_df[
            correspondances_df["code_centre_interet"].isin(centres_codes)
        ][metiers_code_col].unique()
        df.loc[df[metiers_code_col].isin(metiers_ci), "score"] += 3

    # Compétences techniques
    for comp in compet_tech:
        df.loc[df["libelle_rome"].str.contains(comp.split(" / ")[0], case=False, na=False), "score"] += 1

    # Soft skills
    for skill in soft_skills:
        df.loc[df["libelle_rome"].str.contains(skill.split(" ")[0], case=False, na=False), "score"] += 0.5

    # Secteur
    familles_rome = SECTEURS_ROME.get(secteur, [])
    if familles_rome:
        df.loc[df[metiers_code_col].str[:3].isin(familles_rome), "score"] += 2

    # Objectifs
    families_nlp, keywords_nlp = analyse_objectifs_nlp(objectifs)
    if families_nlp:
        df.loc[df[metiers_code_col].str[:3].isin(families_nlp), "score"] += 3
        df.loc[df[metiers_code_col].str[:2].isin([f[:2] for f in families_nlp]), "score"] += 1.5

    return df.sort_values(by="score", ascending=False).head(5), families_nlp, keywords_nlp

# ---------------------
# PDF SAFE + LARGEUR DYNAMIQUE A4
# ---------------------
def safe_text(txt):
    if txt is None:
        return ""
    return str(txt).encode('latin-1', 'replace').decode('latin-1')

def generate_pdf(nom, objectifs, compet_tech, soft_skills, mode_travail, rythme, secteur, suggestions, families_nlp, keywords_nlp):
    pdf = FPDF(format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(left=15, top=15, right=15)
    pdf.add_page()
    pdf.set_font("Courier", "B", 16)
    pdf.cell(0, 10, safe_text("Plan d'action professionnel"), ln=True)
    pdf.set_font("Helvetica", "", 12)

    usable_width = pdf.w - pdf.l_margin - pdf.r_margin

    def section(title):
        pdf.ln(5)
        pdf.set_font("Courier", "B", 13)
        pdf.cell(0, 8, safe_text(title), ln=True)
        pdf.set_font("Helvetica", "", 11)

    section("👤 Profil")
    pdf.multi_cell(usable_width, 7, safe_text(f"Nom : {nom}"))
    pdf.multi_cell(usable_width, 7, safe_text(f"Objectifs : {objectifs}"))
    pdf.multi_cell(usable_width, 7, safe_text(f"Compétences techniques : {', '.join(compet_tech)}"))
    pdf.multi_cell(usable_width, 7, safe_text(f"Compétences transversales : {', '.join(soft_skills)}"))
    pdf.multi_cell(usable_width, 7, safe_text(f"Mode de travail : {mode_travail}"))
    pdf.multi_cell(usable_width, 7, safe_text(f"Rythme : {rythme}"))
    pdf.multi_cell(usable_width, 7, safe_text(f"Secteur préféré : {secteur}"))

    section("🧠 Analyse Poussée")
    if keywords_nlp:
        pdf.multi_cell(usable_width, 7, safe_text(f"Mots-clés détectés : {', '.join(keywords_nlp)}"))
        pdf.multi_cell(usable_width, 7, safe_text(f"Familles ROME associées : {', '.join(families_nlp)}"))
    else:
        pdf.multi_cell(usable_width, 7, "Aucun mot-clé détecté.")

    section("💼 Métiers recommandés")
    for _, row in suggestions.iterrows():
        pdf.multi_cell(usable_width, 7, safe_text(f"- {row['libelle_rome']} (ROME {row['code_rome']}) – Score {row['score']}"))

    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer

# ---------------------
# INTERFACE UTILISATEUR
# ---------------------
if metiers_df is not None:
    with st.form("form_profil"):
        col1, col2 = st.columns(2)

        with col1:
            nom = st.text_input("Nom ou pseudo")
            centres_opts = [
                f"{row['code_centre_interet']} - {row['libelle_centre_interet']}"
                for _, row in centres_interet_df.iterrows()
            ]
            centres_user = st.multiselect("🎯 Centres d’intérêt", centres_opts)
            compet_tech = st.multiselect("🛠️ Compétences techniques", [
                "Informatique / Programmation",
                "Machines / Outils",
                "Construction",
                "Restauration",
                "Soins",
                "Gestion / Administration",
                "Commerce",
            ])

        with col2:
            mode_travail = st.radio("💼 Mode de travail préféré", ["Autonome", "En équipe", "Mixte"])
            rythme = st.radio("⚡ Rythme", ["Calme", "Dynamique", "Variable"])
            secteur = st.selectbox("🏢 Secteur d'activité préféré", list(SECTEURS_ROME.keys()))
            soft_skills = st.multiselect("🌟 Soft skills", [
                "Organisation", "Adaptation", "Communication", "Analyse",
                "Résolution de problèmes", "Esprit d'équipe", "Rigueur",
                "Leadership", "Créativité", "Patience"
            ])

        objectifs = st.text_area("🎯 Vos objectifs professionnels")

        submitted = st.form_submit_button("🔍 Analyser mon profil")

    if submitted:

        suggestions, fam_nlp, kw_nlp = matcher_metiers(
            centres_user, compet_tech, soft_skills, secteur, objectifs
        )

        st.success("Analyse terminée ✔")

        st.subheader("🧠 Analyse Poussée")
        if kw_nlp:
            st.markdown(f"**Mots-clés détectés :** {', '.join(kw_nlp)}")
            st.markdown(f"**Familles ROME associées :** {', '.join(fam_nlp)}")
        else:
            st.info("Aucun mot-clé détecté dans vos objectifs.")

        st.subheader("💼 Métiers recommandés")
        for _, row in suggestions.iterrows():
            with st.expander(f"{row['libelle_rome']} (ROME {row['code_rome']})"):
                st.write(f"Score : **{row['score']}**")
                st.write(f"[Voir la fiche métier](https://candidat.francetravail.fr/metierscope/fiche-metier/{row['code_rome']})")

        pdf_file = generate_pdf(
            nom, objectifs, compet_tech, soft_skills,
            mode_travail, rythme, secteur, suggestions,
            fam_nlp, kw_nlp
        )

        st.download_button(
            "📄 Télécharger le PDF",
            data=pdf_file,
            file_name=f"Plan_Orientation_{nom.replace(' ','_')}.pdf",
            mime="application/pdf"
        )

# FOOTER
st.markdown("---")
st.markdown(
    f"<div style='text-align:center;color:#666;font-size:12px;'>"
    f"Application basée sur ROME – Mise à jour {LAST_UPDATE}"
    "</div>",
    unsafe_allow_html=True
)
