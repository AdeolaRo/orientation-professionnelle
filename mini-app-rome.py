import streamlit as st
import pandas as pd
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from io import BytesIO
from datetime import date

# Configuration de la page
st.set_page_config(page_title="Orientation Professionnelle ROME", page_icon="🎯", layout="wide")

# Titre principal
st.title("🎯 Questionnaire d'Orientation Professionnelle")
st.markdown("**Basé sur les données ROME officielles** - Répertoire Opérationnel des Métiers et des Emplois")

LAST_UPDATE = date.today().strftime("%d-%m-%Y")

# Chargement des données
@st.cache_data
def load_rome_data():
    try:
        metiers_df = pd.read_csv('RefRomeCsv/unix_referentiel_code_rome_v460_utf8.csv')
        competences_df = pd.read_csv('RefRomeCsv/unix_referentiel_competence_v460_utf8.csv')
        centres_interet_df = pd.read_csv('RefRomeCsv/unix_centre_interet_v460_utf8.csv')
        correspondances_df = pd.read_csv('RefRomeCsv/unix_lien_centre_metier.csv')  # ajout ici
        return metiers_df, competences_df, centres_interet_df, correspondances_df
    except Exception as e:
        st.error(f"Erreur lors du chargement des données ROME : {e}")
        return None, None, None, None

# Fonction de matching améliorée
def matcher_metiers(metiers_df, correspondances_df, centres_interet_selection, competences_tech, soft_skills, secteur):
    codes_centre_selectionnes = [ci.split(" - ")[0] for ci in centres_interet_selection]
    metiers_associes = correspondances_df[
        correspondances_df["code_centre_interet"].isin(codes_centre_selectionnes)
    ]["code_rome"].unique()
    metiers_filtres = metiers_df[metiers_df["code_rome"].isin(metiers_associes)].copy()

    if metiers_filtres.empty:
        sample_df = metiers_df.sample(5).copy()
        sample_df["score"] = 0
        return sample_df

    # Initialisation de la colonne score
    metiers_filtres["score"] = 0

    for i, row in metiers_filtres.iterrows():
        score = 0
        libelle = str(row["libelle_rome"]).lower()

        for c in competences_tech:
            if c.lower() in libelle:
                score += 1

        for s in soft_skills:
            if s.lower() in libelle:
                score += 0.5

        if secteur.lower() in libelle:
            score += 1

        metiers_filtres.at[i, "score"] = score

    return metiers_filtres.sort_values(by="score", ascending=False).head(5)

# Chargement des données
metiers_df, competences_df, centres_interet_df, correspondances_df = load_rome_data()

if metiers_df is not None and correspondances_df is not None:
    # Interface utilisateur
    with st.form("profil_form"):
        st.subheader("📋 Votre Profil")
        col1, col2 = st.columns(2)

        with col1:
            nom = st.text_input("Votre nom ou pseudo")

            st.subheader("🎯 Centres d'intérêt")
            centres_interet_options = []
            if centres_interet_df is not None:
                for _, row in centres_interet_df.iterrows():
                    centres_interet_options.append(f"{row['code_centre_interet']} - {row['libelle_centre_interet']}")
            centres_interet_selection = st.multiselect("Quels centres d'intérêt vous correspondent le mieux ?",
                                                       centres_interet_options[:10])

            st.subheader("🛠️ Compétences techniques")
            competences_tech = st.multiselect("Quelles compétences techniques possédez-vous ?", [
                "Informatique / Numérique", "Machines / Outils", "Véhicules / Conduite",
                "Bâtiment / Construction", "Cuisine / Restauration", "Soins / Santé",
                "Commerce / Vente", "Administration / Gestion"
            ])

        with col2:
            st.subheader("💼 Préférences de travail")
            mode_travail = st.radio("Mode de travail préféré :", ["Autonome", "En équipe", "Mixte"])
            rythme = st.radio("Rythme de travail :", ["Calme et régulier", "Dynamique", "Variable"])
            secteur = st.selectbox("Secteur d'activité préféré :", [
                "Tous secteurs", "Agriculture / Environnement", "Artisanat / BTP", "Commerce / Vente",
                "Santé / Social", "Transport / Logistique", "Informatique / Numérique", "Administration / Services"
            ])
            formation = st.text_input("Formation ou diplôme (facultatif)")

        st.subheader("🌟 Compétences transversales")
        soft_skills = st.multiselect("Sélectionnez vos compétences transversales :", [
            "Sens de l'organisation", "Capacité d'adaptation", "Communication", "Esprit d'analyse",
            "Résolution de problèmes", "Esprit d'équipe", "Précision / Rigueur", "Leadership",
            "Créativité", "Patience"
        ])

        st.subheader("🎯 Vos objectifs")
        objectifs = st.text_area("Décrivez vos objectifs professionnels :",
                                 placeholder="Ex: Trouver un emploi dans le secteur de la santé...")

        submitted = st.form_submit_button("🔍 Analyser mon profil et obtenir des suggestions")

    if submitted:
        st.success("✅ Profil analysé ! Voici vos suggestions personnalisées :")

        st.subheader("💼 Métiers suggérés")

        suggestions_metiers = matcher_metiers(
            metiers_df,
            correspondances_df,
            centres_interet_selection,
            competences_tech,
            soft_skills,
            secteur
        )

        for _, metier in suggestions_metiers.iterrows():
            code_rome = metier["code_rome"]
            libelle = metier["libelle_rome"]
            url = f"https://candidat.francetravail.fr/metierscope/fiche-metier/{code_rome}"
            score = metier.get("score", 0) 

            with st.expander(f"**{libelle}** (ROME : {code_rome})"):
                st.write(f"🔗 [Voir la fiche métier]({url})")
                st.write(f"🧮 **Score de pertinence :** {score}/3")
                st.write(f"🔍 **Description :** {metier.get('description_rome', 'Non disponible')}")

        st.subheader("📋 Plan d'action personnalisé")
        plan_html = f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3 style="color: #1f77b4; margin-top: 0;">📋 Plan d'action personnalisé</h3>
            <p><strong>👤 Nom :</strong> {nom}</p>
            <p><strong>🎯 Objectifs :</strong> {objectifs if objectifs else 'Non précisé'}</p>
            <p><strong>🛠️ Compétences techniques :</strong> {', '.join(competences_tech) if competences_tech else 'Non spécifiées'}</p>
            <p><strong>🌟 Compétences transversales :</strong> {', '.join(soft_skills) if soft_skills else 'Non spécifiées'}</p>
            <p><strong>💼 Mode de travail préféré :</strong> {mode_travail}</p>
            <p><strong>⚡ Rythme de travail :</strong> {rythme}</p>
            <p><strong>🏢 Secteur d'activité :</strong> {secteur}</p>
        </div>
        """
        st.markdown(plan_html, unsafe_allow_html=True)

        if st.button("📄 Télécharger le plan d'action (PDF)"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Helvetica", "B", 16)
            pdf.cell(0, 10, "Plan d'action personnalisé - Orientation Professionnelle", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

            pdf.set_font("Helvetica", "", 12)
            pdf.cell(0, 10, f"Nom: {nom}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.cell(0, 10, f"Objectifs: {objectifs if objectifs else 'Non précisé'}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.cell(0, 10, f"Compétences techniques: {', '.join(competences_tech) if competences_tech else 'Non spécifiées'}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.cell(0, 10, f"Compétences transversales: {', '.join(soft_skills) if soft_skills else 'Non spécifiées'}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

            pdf.ln(10)
            pdf.set_font("Helvetica", "B", 14)
            pdf.cell(0, 10, "Métiers suggérés :", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

            pdf.set_font("Helvetica", "", 11)
            for _, metier in suggestions_metiers.iterrows():
                pdf.cell(0, 8, f"- {metier['libelle_rome']} (ROME {metier['code_rome']})", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

            buffer = BytesIO()
            pdf.output(buffer)
            buffer.seek(0)

            st.download_button("📄 Télécharger le plan d'action (PDF)", buffer, file_name=f"Plan_Orientation_{nom.replace(' ', '_')}.pdf", mime="application/pdf")

else:
    st.error("❌ Impossible de charger les données ROME. Vérifiez que tous les fichiers CSV sont présents.")

# Pied de page
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px;">
    🎯 Application d'orientation professionnelle basée sur les données ROME officielles<br>
    st.write(f"Dernière mise à jour : {LAST_UPDATE}")<br>
    ROME - France Travail
</div>
""", unsafe_allow_html=True)
