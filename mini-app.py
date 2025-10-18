import streamlit as st
import pandas as pd
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from io import BytesIO

# Dictionnaire simplifié des correspondances
mapping = {
    "Accueil du public": ("D1407", "Agent d'accueil"),
    "Utilisation de machines": ("H2903", "Conducteur de machines"),
    "Soin aux personnes": ("K1302", "Aide-soignant"),
    "Organisation / logistique": ("N1103", "Agent logistique"),
    "Telephone / contact client": ("M1606", "Teleconseiller"),
    "Animation": ("G1202", "Animateur socioculturel"),
    "Conduite": ("N4101", "Chauffeur livreur"),
    "Bricolage": ("F1606", "Ouvrier polyvalent d'entretien"),
    "Vente / negociation": ("D1406", "Vendeur conseil"),
    "Informatique / bureautique": ("M1805", "Technicien support informatique"),
}

# Interface
st.set_page_config(page_title="Orientation Métiers", page_icon="🎯")
st.title("🎯 Questionnaire : Profil de Competences & Orientation Metiers")

with st.form("profil_form"):
    nom = st.text_input("Votre nom ou pseudo")

    taches = st.multiselect("1. Quelles taches realisez-vous le plus souvent ?", list(mapping.keys()))

    domaines = st.multiselect("2. Domaine(s) ou vous vous sentez a l'aise ?", [
        "Technique / manuel", "Relationnel / service a la personne",
        "Organisation / gestion", "Creation / art / esthetique",
        "Numerique / informatique", "Environnement / nature", "Aucune preference"
    ])

    mode_travail = st.radio("3. Preferez-vous travailler :", ["Autonome", "En equipe", "Peu importe"])

    rythme = st.radio("4. Quel rythme de travail vous convient le mieux ?", ["Calme", "Dynamique", "Variable"])

    soft_skills = st.multiselect("5. Competences transversales", [
        "Sens de l'organisation", "Capacite d'adaptation", "Sens de la communication",
        "Esprit d'analyse", "Resolution de problemes", "Esprit d'equipe", "Precision / rigueur"
    ])

    outils = st.multiselect("6. Environnements familiers", [
        "Ordinateur / bureautique", "Outils manuels / machines",
        "Telephone / contact client", "Vehicules / conduite", "Aucun en particulier"
    ])

    formation = st.text_input("7. Formation ou diplome (facultatif)")

    conditions = st.multiselect("8. Conditions de travail souhaitees", [
        "Travail en interieur", "Travail en exterieur",
        "Horaires fixes", "Horaires variables",
        "Station debout", "Poste assis"
    ])

    metiers_souhaites = st.text_area("9. Metiers qui vous attirent (meme sans experience)")

    formation_futur = st.radio("10. Pret(e) a vous former pour changer de metier ?", ["Oui", "Peut-etre", "Non"])

    submitted = st.form_submit_button("🎁 Generer mes suggestions & plan d'action")

if submitted:
    st.subheader("🔍 Suggestions metiers")
    suggestions = []
    for t in taches:
        if t in mapping:
            code, metier = mapping[t]
            url = f"https://candidat.francetravail.fr/metiers/{code}"
            suggestions.append((metier, code, url))
            st.markdown(f"- **{metier}** (ROME : `{code}`) – [Fiche]({url})")

    st.subheader("🗂️ Plan d'action personnalise")
    st.markdown(f"""
    - **Nom / Pseudo :** {nom}
    - **Objectif metier(s) vise(s) :** {metiers_souhaites if metiers_souhaites else "Non precise"}
    - **Formations a envisager :** {"Oui" if formation_futur == "Oui" else "A discuter"}
    - **Competences a valoriser :** {", ".join(soft_skills)}
    - **Types de poste :** {", ".join(domaines)} / {", ".join(taches)}
    """)

    # PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Plan d'action personnalise", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 10, f"Nom / Pseudo : {nom}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, f"Metiers suggeres :", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    for metier, code, _ in suggestions:
        pdf.cell(0, 10, f"- {metier} (ROME {code})", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.ln(5)
    pdf.cell(0, 10, f"Objectif metier(s) : {metiers_souhaites}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, f"Competences transversales : {', '.join(soft_skills)}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, f"Formations : {formation}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, f"Pret a se former : {formation_futur}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)

    st.download_button("📄 Telecharger le plan d'action (PDF)", buffer, file_name=f"Plan_{nom.replace(' ', '_')}.pdf", mime="application/pdf")
