import streamlit as st
import pandas as pd
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from io import BytesIO
import os

# Configuration de la page
st.set_page_config(
    page_title="Orientation Professionnelle ROME", 
    page_icon="🎯",
    layout="wide"
)

# Titre principal
st.title("🎯 Questionnaire d'Orientation Professionnelle")
st.markdown("**Basé sur les données ROME officielles** - Répertoire Opérationnel des Métiers et des Emplois")

# Chargement des données ROME
@st.cache_data
def load_rome_data():
    """Charge les données ROME depuis les fichiers CSV"""
    try:
        # Charger les métiers
        metiers_df = pd.read_csv('RefRomeCsv/unix_referentiel_code_rome_v460_utf8.csv')
        
        # Charger les compétences
        competences_df = pd.read_csv('RefRomeCsv/unix_referentiel_competence_v460_utf8.csv')
        
        # Charger les centres d'intérêt
        centres_interet_df = pd.read_csv('RefRomeCsv/unix_centre_interet_v460_utf8.csv')
        
        return metiers_df, competences_df, centres_interet_df
    except Exception as e:
        st.error(f"Erreur lors du chargement des données ROME : {e}")
        return None, None, None

# Charger les données
metiers_df, competences_df, centres_interet_df = load_rome_data()

if metiers_df is not None:
    # Interface utilisateur
    with st.form("profil_form"):
        st.subheader("📋 Votre Profil")
        
        col1, col2 = st.columns(2)
        
        with col1:
            nom = st.text_input("Votre nom ou pseudo")
            
            # Centres d'intérêt ROME
            st.subheader("🎯 Centres d'intérêt")
            centres_interet_options = []
            if centres_interet_df is not None:
                for _, row in centres_interet_df.iterrows():
                    centres_interet_options.append(f"{row['code_centre_interet']} - {row['libelle_centre_interet']}")
            
            centres_interet_selection = st.multiselect(
                "Quels centres d'intérêt vous correspondent le mieux ?",
                centres_interet_options[:10],  # Limiter à 10 pour l'interface
                help="Sélectionnez les domaines qui vous intéressent le plus"
            )
            
            # Compétences techniques
            st.subheader("🛠️ Compétences techniques")
            competences_tech = st.multiselect(
                "Quelles compétences techniques possédez-vous ?",
                [
                    "Informatique / Numérique",
                    "Machines / Outils",
                    "Véhicules / Conduite", 
                    "Bâtiment / Construction",
                    "Cuisine / Restauration",
                    "Soins / Santé",
                    "Commerce / Vente",
                    "Administration / Gestion"
                ]
            )
        
        with col2:
            # Préférences de travail
            st.subheader("💼 Préférences de travail")
            
            mode_travail = st.radio(
                "Mode de travail préféré :",
                ["Autonome", "En équipe", "Mixte"]
            )
            
            rythme = st.radio(
                "Rythme de travail :",
                ["Calme et régulier", "Dynamique", "Variable"]
            )
            
            secteur = st.selectbox(
                "Secteur d'activité préféré :",
                [
                    "Tous secteurs",
                    "Agriculture / Environnement",
                    "Artisanat / BTP",
                    "Commerce / Vente",
                    "Santé / Social",
                    "Transport / Logistique",
                    "Informatique / Numérique",
                    "Administration / Services"
                ]
            )
            
            formation = st.text_input("Formation ou diplôme (facultatif)")
        
        # Compétences transversales
        st.subheader("🌟 Compétences transversales")
        soft_skills = st.multiselect(
            "Sélectionnez vos compétences transversales :",
            [
                "Sens de l'organisation",
                "Capacité d'adaptation", 
                "Communication",
                "Esprit d'analyse",
                "Résolution de problèmes",
                "Esprit d'équipe",
                "Précision / Rigueur",
                "Leadership",
                "Créativité",
                "Patience"
            ]
        )
        
        # Objectifs
        st.subheader("🎯 Vos objectifs")
        objectifs = st.text_area(
            "Décrivez vos objectifs professionnels :",
            placeholder="Ex: Trouver un emploi dans le secteur de la santé, me reconvertir dans l'informatique..."
        )
        
        submitted = st.form_submit_button("🔍 Analyser mon profil et obtenir des suggestions")

    # Traitement des résultats
    if submitted:
        st.success("✅ Profil analysé ! Voici vos suggestions personnalisées :")
        
        # Simulation d'analyse basée sur les données ROME
        st.subheader("📊 Analyse de votre profil")
        
        # Affichage des centres d'intérêt sélectionnés
        if centres_interet_selection:
            st.write("**Centres d'intérêt identifiés :**")
            for centre in centres_interet_selection:
                st.write(f"• {centre}")
        
        # Suggestions de métiers basées sur les données ROME
        st.subheader("💼 Métiers suggérés")
        
        # Filtrer les métiers selon les critères
        suggestions_metiers = []
        
        if metiers_df is not None:
            # Exemple de logique de suggestion (à adapter selon vos besoins)
            if "Agriculture" in str(centres_interet_selection) or "Environnement" in str(centres_interet_selection):
                suggestions_metiers = metiers_df[metiers_df['code_rome'].str.startswith('A')].head(5)
            elif "Commerce" in str(centres_interet_selection) or "Vente" in str(competences_tech):
                suggestions_metiers = metiers_df[metiers_df['code_rome'].str.startswith('D')].head(5)
            elif "Santé" in str(competences_tech) or "Soins" in str(competences_tech):
                suggestions_metiers = metiers_df[metiers_df['code_rome'].str.startswith('K')].head(5)
            else:
                # Suggestions générales
                suggestions_metiers = metiers_df.head(5)
        
        # Affichage des suggestions
        if not suggestions_metiers.empty:
            for _, metier in suggestions_metiers.iterrows():
                code_rome = metier['code_rome']
                libelle = metier['libelle_rome']
                url = f"https://candidat.francetravail.fr/metierscope/fiche-metier/{code_rome}"
                
                with st.expander(f"**{libelle}** (Code ROME: {code_rome})"):
                    st.write(f"🔗 [Voir la fiche métier complète]({url})")
                    
                    # Informations sur les transitions
                    if pd.notna(metier['transition_eco']):
                        st.write(f"🌱 **Transition écologique :** {metier['transition_eco']}")
                    if pd.notna(metier['transition_num']):
                        st.write(f"💻 **Transition numérique :** {metier['transition_num']}")
                    if pd.notna(metier['transition_demo']):
                        st.write(f"👥 **Transition démographique :** {metier['transition_demo']}")
        
        # Plan d'action personnalisé
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
        
        # Génération du PDF
        if st.button("📄 Télécharger le plan d'action (PDF)"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Helvetica", "B", 16)
            pdf.cell(0, 10, "Plan d'action personnalise - Orientation Professionnelle", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            pdf.set_font("Helvetica", "", 12)
            pdf.cell(0, 10, f"Nom: {nom}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.cell(0, 10, f"Objectifs: {objectifs if objectifs else 'Non precise'}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.cell(0, 10, f"Competences techniques: {', '.join(competences_tech) if competences_tech else 'Non specifiees'}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.cell(0, 10, f"Competences transversales: {', '.join(soft_skills) if soft_skills else 'Non specifiees'}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            pdf.ln(10)
            pdf.set_font("Helvetica", "B", 14)
            pdf.cell(0, 10, "Metiers suggeres:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            pdf.set_font("Helvetica", "", 11)
            for _, metier in suggestions_metiers.iterrows():
                pdf.cell(0, 8, f"- {metier['libelle_rome']} (ROME {metier['code_rome']})", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            buffer = BytesIO()
            pdf.output(buffer)
            buffer.seek(0)
            
            st.download_button(
                "📄 Télécharger le plan d'action (PDF)", 
                buffer, 
                file_name=f"Plan_Orientation_{nom.replace(' ', '_')}.pdf", 
                mime="application/pdf"
            )

else:
    st.error("❌ Impossible de charger les données ROME. Vérifiez que le dossier RefRomeCSV est présent.")

# Pied de page
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px;">
    🎯 Application d'orientation professionnelle basée sur les données ROME officielles<br>
    Répertoire Opérationnel des Métiers et des Emplois - France Travail
</div>
""", unsafe_allow_html=True)
